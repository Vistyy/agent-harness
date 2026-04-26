#!/usr/bin/env python3
# ruff: noqa: T201
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import cast

SKIP_DIR_NAMES = frozenset(
    {
        ".git",
        ".next",
        ".venv",
        ".dart_tool",
        "build",
        "coverage",
        "dist",
        "node_modules",
        "test-results",
    }
)

GIANT_SUITE_LINES = 1500
OVERSIZED_FILE_LINES = 800
LARGE_FILE_LINES = 400
TOP_CASES = 40
MID_CASES = 20
MIN_CASES = 12
MIN_ASSERTIONS = 3
HEAVY_MOCKS = 30
MID_MOCKS = 12
HEAVY_WAITS = 20
MID_WAITS = 8
LIGHT_WAITS = 4
HEAVY_SKIPS = 4
HEAVY_SNAPSHOTS = 4
MID_SNAPSHOTS = 2
OVERSCOPED_FIXTURES = 10
RUNNER_HEAVY = 2
RETRYING_RUNNER = 1
WEB_ORCHESTRATION_MOCKS = 20
WEB_ORCHESTRATION_WAITS = 8
PYTHON_WAIT_RISK = 8
MIN_MOBILE_CLUSTER_PARTS = 5


@dataclass(frozen=True)
class PatternSet:
    cases: re.Pattern[str]
    assertions: re.Pattern[str]
    mocks: re.Pattern[str]
    waits: re.Pattern[str]
    skips: re.Pattern[str]
    snapshots: re.Pattern[str]
    fixtures: re.Pattern[str]
    runner_bound: re.Pattern[str]


@dataclass(frozen=True)
class TestFileAudit:
    path: str
    framework: str
    layer: str
    cluster: str
    lines: int
    cases: int
    assertions: int
    mocks: int
    waits: int
    skips: int
    snapshots: int
    fixtures: int
    runner_bound: int
    suspicion_score: int
    reasons: tuple[str, ...]


@dataclass(frozen=True)
class AuditMetrics:
    lines: int
    cases: int
    assertions: int
    mocks: int
    waits: int
    skips: int
    snapshots: int
    fixtures: int
    runner_bound: int


@dataclass(frozen=True)
class ClusterAudit:
    cluster: str
    files: int
    frameworks: tuple[str, ...]
    total_score: int
    max_file_score: int
    reasons: tuple[str, ...]
    largest_file: str


@dataclass(frozen=True)
class CorpusSummary:
    total_files: int
    suspicious_files: int
    framework_counts: dict[str, int]
    cluster_count: int


PATTERNS = {
    "python": PatternSet(
        cases=re.compile(r"(?m)^\s*(?:async\s+)?def test_[a-zA-Z0-9_]+\s*\("),
        assertions=re.compile(r"\bassert\b|pytest\.raises\(|pytest\.fail\(|self\.assert[A-Za-z]+\("),
        mocks=re.compile(r"\bmonkeypatch\b|\bMock\(|\bMagicMock\(|\bAsyncMock\(|\bpatch\(|\bspy\("),
        waits=re.compile(r"\bsleep\(|\bwait_for\(|\bwait_until\("),
        skips=re.compile(r"pytest\.(?:skip|xfail)\(|@pytest\.mark\.(?:skip|skipif|xfail)"),
        snapshots=re.compile(r"$^"),
        fixtures=re.compile(r"@pytest\.fixture"),
        runner_bound=re.compile(r"subprocess\.(?:run|Popen)\(|testcontainers|docker|playwright|webdriver"),
    ),
    "web": PatternSet(
        cases=re.compile(r"\b(?:it|test)\s*\("),
        assertions=re.compile(r"\bexpect\s*\("),
        mocks=re.compile(r"\bvi\.(?:fn|mock|spyOn)\(|mock(?:Resolved|Rejected|Return|Implementation)Value"),
        waits=re.compile(r"waitFor\(|findBy[A-Z]|advanceTimersByTime\(|runAllTimers\("),
        skips=re.compile(r"\b(?:it|test|describe)\.(?:skip|todo)\("),
        snapshots=re.compile(r"toMatch(?:Inline)?Snapshot\(|toMatchFileSnapshot\("),
        fixtures=re.compile(r"\bbeforeEach\(|\bafterEach\("),
        runner_bound=re.compile(r"playwright|puppeteer|webdriver"),
    ),
    "mobile": PatternSet(
        cases=re.compile(r"\btest(?:Widgets)?\s*\("),
        assertions=re.compile(r"\bexpect\s*\("),
        mocks=re.compile(r"\bwhen\s*\(|\bverify\s*\(|Mock[A-Z]\w+"),
        waits=re.compile(r"pumpAndSettle\(|Future\.delayed\(|\bsleep\("),
        skips=re.compile(r"skip:\s*true"),
        snapshots=re.compile(r"matchesGoldenFile\("),
        fixtures=re.compile(r"\bsetUp(?:All)?\(|\btearDown(?:All)?\("),
        runner_bound=re.compile(r"integration_test|patrol|maestro|appium|webdriver"),
    ),
}


def _default_repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def _is_test_file(path: Path) -> bool:
    name = path.name
    if name.endswith((".test.ts", ".spec.ts", ".test.js", ".spec.js", "_test.dart")):
        return True
    if not ((name.startswith("test_") or name.endswith("_test.py")) and path.suffix == ".py"):
        return False
    return _is_python_test_path(path)


def _is_python_test_path(path: Path) -> bool:
    parts = path.parts
    return "tests" in parts or "test" in parts


def _framework_for_path(path: Path) -> str | None:
    name = path.name
    if (name.startswith("test_") and path.suffix == ".py") or name.endswith("_test.py"):
        return "python"
    if name.endswith((".test.ts", ".spec.ts", ".test.js", ".spec.js")):
        return "web"
    if name.endswith("_test.dart"):
        return "mobile"
    return None


def _infer_layer(path: Path, framework: str) -> str:
    joined = "/".join(path.parts)
    layer = "unknown"
    if "/integration_test/" in joined:
        layer = "integration"
    elif "/tests/e2e/" in joined:
        layer = "e2e"
    elif "/tests/integration/" in joined:
        layer = "integration"
    elif "/tests/contract/" in joined:
        layer = "contract"
    elif "/tests/unit/" in joined:
        layer = "unit"
    elif framework == "web" and "/__tests__/" in joined:
        layer = "unit-or-component"
    elif framework == "mobile" and "/test/" in joined:
        layer = "widget-or-unit"
    return layer


def _infer_cluster(path: Path, framework: str) -> str:
    parts = path.parts
    if "__tests__" in parts:
        index = parts.index("__tests__")
        return "/".join(parts[: index + 1])
    if (
        framework == "mobile"
        and len(parts) >= MIN_MOBILE_CLUSTER_PARTS
        and parts[0] == "apps"
        and parts[1] == "mobile"
        and parts[2] in {"test", "integration_test"}
    ):
        return "/".join(parts[:-1])
    return str(path.parent).replace("\\", "/")


def _count(pattern: re.Pattern[str], text: str) -> int:
    return len(pattern.findall(text))


def _apply_first_match(
    score: int,
    reasons: list[str],
    value: int,
    rules: tuple[tuple[int, int, str], ...],
) -> tuple[int, list[str]]:
    for minimum, points, reason in rules:
        if value >= minimum:
            score += points
            reasons.append(reason)
            break
    return score, reasons


def _score_audit(
    *,
    framework: str,
    layer: str,
    metrics: AuditMetrics,
) -> tuple[int, tuple[str, ...]]:
    score = 0
    reasons: list[str] = []

    score, reasons = _apply_first_match(
        score,
        reasons,
        metrics.lines,
        (
            (GIANT_SUITE_LINES, 6, "giant-suite"),
            (OVERSIZED_FILE_LINES, 4, "oversized-file"),
            (LARGE_FILE_LINES, 2, "oversized-file"),
        ),
    )
    score, reasons = _apply_first_match(
        score,
        reasons,
        metrics.cases,
        (
            (TOP_CASES, 5, "too-many-cases"),
            (MID_CASES, 3, "too-many-cases"),
            (MIN_CASES, 1, "too-many-cases"),
        ),
    )

    if metrics.assertions < max(MIN_ASSERTIONS, metrics.cases):
        score += 3
        reasons.append("assertion-thin")
    elif metrics.cases >= MIN_CASES and metrics.assertions < metrics.cases * 2:
        score += 1
        reasons.append("assertion-thin")

    score, reasons = _apply_first_match(
        score,
        reasons,
        metrics.mocks,
        (
            (HEAVY_MOCKS, 5, "heavy-mock-surface"),
            (MID_MOCKS, 3, "heavy-mock-surface"),
        ),
    )
    score, reasons = _apply_first_match(
        score,
        reasons,
        metrics.waits,
        (
            (HEAVY_WAITS, 5, "wait-heavy"),
            (MID_WAITS, 3, "wait-heavy"),
            (LIGHT_WAITS, 1, "wait-heavy"),
        ),
    )

    if metrics.skips >= HEAVY_SKIPS:
        score += 2
        reasons.append("skip-heavy")

    score, reasons = _apply_first_match(
        score,
        reasons,
        metrics.snapshots,
        (
            (HEAVY_SNAPSHOTS, 4, "snapshot-or-golden"),
            (MID_SNAPSHOTS, 2, "snapshot-or-golden"),
        ),
    )

    if metrics.fixtures >= OVERSCOPED_FIXTURES:
        score += 2
        reasons.append("overscoped-fixtures")

    score, reasons = _apply_first_match(
        score,
        reasons,
        metrics.runner_bound,
        (
            (RUNNER_HEAVY, 4, "runner-heavy"),
            (RETRYING_RUNNER, 2, "runner-heavy"),
        ),
    )

    if layer == "unit" and (metrics.runner_bound > 0 or (framework == "python" and metrics.waits >= PYTHON_WAIT_RISK)):
        score += 3
        reasons.append("wrong-layer-risk")

    if framework == "web" and metrics.mocks >= WEB_ORCHESTRATION_MOCKS and metrics.waits >= WEB_ORCHESTRATION_WAITS:
        score += 2
        reasons.append("orchestration-overfit")

    unique_reasons = tuple(dict.fromkeys(reasons))
    return score, unique_reasons


def collect_test_file_audits(*, repo_root: Path) -> tuple[TestFileAudit, ...]:
    audits: list[TestFileAudit] = []
    for path in sorted(repo_root.rglob("*")):
        if not path.is_file() or any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        if not _is_test_file(path):
            continue
        framework = _framework_for_path(path)
        if framework is None:
            continue
        patterns = PATTERNS[framework]
        relative_path = path.relative_to(repo_root)
        text = path.read_text(encoding="utf-8", errors="ignore")
        layer = _infer_layer(relative_path, framework)
        lines = text.count("\n") + 1
        cases = _count(patterns.cases, text)
        assertions = _count(patterns.assertions, text)
        mocks = _count(patterns.mocks, text)
        waits = _count(patterns.waits, text)
        skips = _count(patterns.skips, text)
        snapshots = _count(patterns.snapshots, text)
        fixtures = _count(patterns.fixtures, text)
        runner_bound = _count(patterns.runner_bound, text)
        suspicion_score, reasons = _score_audit(
            framework=framework,
            layer=layer,
            metrics=AuditMetrics(
                lines=lines,
                cases=cases,
                assertions=assertions,
                mocks=mocks,
                waits=waits,
                skips=skips,
                snapshots=snapshots,
                fixtures=fixtures,
                runner_bound=runner_bound,
            ),
        )
        audits.append(
            TestFileAudit(
                path=str(relative_path).replace("\\", "/"),
                framework=framework,
                layer=layer,
                cluster=_infer_cluster(relative_path, framework),
                lines=lines,
                cases=cases,
                assertions=assertions,
                mocks=mocks,
                waits=waits,
                skips=skips,
                snapshots=snapshots,
                fixtures=fixtures,
                runner_bound=runner_bound,
                suspicion_score=suspicion_score,
                reasons=reasons,
            )
        )
    return tuple(audits)


def cluster_audits(*, audits: tuple[TestFileAudit, ...]) -> tuple[ClusterAudit, ...]:
    grouped: dict[str, list[TestFileAudit]] = defaultdict(list)
    for audit in audits:
        grouped[audit.cluster].append(audit)

    results: list[ClusterAudit] = []
    for cluster, items in grouped.items():
        reason_counts: Counter[str] = Counter()
        frameworks: set[str] = set()
        largest = max(items, key=lambda item: item.lines)
        for item in items:
            frameworks.add(item.framework)
            reason_counts.update(item.reasons)
        results.append(
            ClusterAudit(
                cluster=cluster,
                files=len(items),
                frameworks=tuple(sorted(frameworks)),
                total_score=sum(item.suspicion_score for item in items),
                max_file_score=max(item.suspicion_score for item in items),
                reasons=tuple(reason for reason, _ in reason_counts.most_common(4)),
                largest_file=largest.path,
            )
        )
    return tuple(sorted(results, key=lambda item: (-item.total_score, -item.max_file_score, item.cluster)))


def summarize_audit(*, audits: tuple[TestFileAudit, ...], clusters: tuple[ClusterAudit, ...]) -> CorpusSummary:
    framework_counts: Counter[str] = Counter(audit.framework for audit in audits)
    suspicious_files = sum(1 for audit in audits if audit.suspicion_score > 0)
    return CorpusSummary(
        total_files=len(audits),
        suspicious_files=suspicious_files,
        framework_counts=dict(sorted(framework_counts.items())),
        cluster_count=len(clusters),
    )


def build_markdown_report(
    *,
    summary: CorpusSummary,
    clusters: tuple[ClusterAudit, ...],
    audits: tuple[TestFileAudit, ...],
    top: int,
) -> str:
    lines = [
        "# Test Suite Audit",
        "",
        "## Summary",
        f"- Total test files: `{summary.total_files}`",
        f"- Suspicious files with non-zero score: `{summary.suspicious_files}`",
        f"- Clusters: `{summary.cluster_count}`",
        f"- Framework counts: `{', '.join(f'{name}={count}' for name, count in summary.framework_counts.items())}`",
        "",
        "## Top Clusters",
        "",
        "| Score | Files | Cluster | Frameworks | Reasons | Largest file |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for cluster in clusters[:top]:
        lines.extend(
            [
                "".join(
                    [
                        f"| {cluster.total_score} | {cluster.files} | `{cluster.cluster}` | ",
                        f"`{', '.join(cluster.frameworks)}` | `{', '.join(cluster.reasons)}` | `{cluster.largest_file}` |",
                    ]
                )
            ]
        )

    lines.extend(
        [
            "",
            "## Top Files",
            "",
            "| Score | Framework | Path | Cases | Assertions | Mocks | Waits | Reasons |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for audit in sorted(audits, key=lambda item: (-item.suspicion_score, -item.lines, item.path))[:top]:
        lines.extend(
            [
                "".join(
                    [
                        f"| {audit.suspicion_score} | `{audit.framework}` | `{audit.path}` | {audit.cases} | {audit.assertions} | ",
                        f"{audit.mocks} | {audit.waits} | `{', '.join(audit.reasons)}` |",
                    ]
                )
            ]
        )
    lines.append("")
    return "\n".join(lines)


def _write_text(*, path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    _ = path.write_text(content, encoding="utf-8")


def _json_payload(
    *,
    summary: CorpusSummary,
    clusters: tuple[ClusterAudit, ...],
    audits: tuple[TestFileAudit, ...],
    top: int,
) -> dict[str, object]:
    return {
        "summary": asdict(summary),
        "top_clusters": [asdict(cluster) for cluster in clusters[:top]],
        "top_files": [
            asdict(audit) for audit in sorted(audits, key=lambda item: (-item.suspicion_score, -item.lines, item.path))[:top]
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Inventory and score suspicious test clusters across the repo.")
    _ = parser.add_argument("--repo-root", type=Path, default=_default_repo_root())
    _ = parser.add_argument("--top", type=int, default=25)
    _ = parser.add_argument("--markdown-output", type=Path)
    _ = parser.add_argument("--json-output", type=Path)
    args = parser.parse_args()

    repo_root = cast(Path, args.repo_root).resolve()
    top = cast(int, args.top)
    markdown_output = cast(Path | None, args.markdown_output)
    json_output = cast(Path | None, args.json_output)
    audits = collect_test_file_audits(repo_root=repo_root)
    clusters = cluster_audits(audits=audits)
    summary = summarize_audit(audits=audits, clusters=clusters)
    markdown = build_markdown_report(summary=summary, clusters=clusters, audits=audits, top=top)

    if markdown_output is not None:
        _write_text(path=markdown_output, content=markdown)
    else:
        print(markdown)

    if json_output is not None:
        payload = _json_payload(summary=summary, clusters=clusters, audits=audits, top=top)
        _write_text(path=json_output, content=json.dumps(payload, indent=2, sort_keys=True) + "\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
