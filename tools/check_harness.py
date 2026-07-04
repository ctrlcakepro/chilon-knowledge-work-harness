from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import math
import re
import sys


ROOT = Path(__file__).resolve().parents[1]


@dataclass
class CheckResult:
    level: str
    name: str
    detail: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def add(results: list[CheckResult], level: str, name: str, detail: str) -> None:
    results.append(CheckResult(level=level, name=name, detail=detail))


def approx_token_count(text: str) -> int:
    """Conservative mixed-language token estimate without external deps."""
    ascii_chars = len(re.findall(r"[\x00-\x7F]", text))
    cjk_chars = len(re.findall(r"[\u4e00-\u9fff]", text))
    other_chars = max(0, len(text) - ascii_chars - cjk_chars)
    return math.ceil(ascii_chars / 3.2 + cjk_chars * 1.15 + other_chars / 2.2)


def check_exists(results: list[CheckResult], rel_path: str) -> None:
    path = ROOT / rel_path
    if path.exists():
        add(results, "PASS", f"存在性: {rel_path}", "文件或目录存在。")
    else:
        add(results, "FAIL", f"存在性: {rel_path}", "缺失，当前 package 不完整。")


def check_contains(results: list[CheckResult], rel_path: str, needles: list[str], label: str) -> None:
    path = ROOT / rel_path
    if not path.exists():
        add(results, "FAIL", label, f"{rel_path} 不存在，无法检查。")
        return
    content = read_text(path)
    missing = [needle for needle in needles if needle not in content]
    if missing:
        add(results, "FAIL", label, f"缺少关键段落: {', '.join(missing)}")
    else:
        add(results, "PASS", label, "关键段落完整。")


def iter_text_files() -> list[Path]:
    suffixes = {".md", ".toml", ".ps1", ".cmd", ".py"}
    ignored_parts = {".git", "__pycache__", "outputs", ".harness-install-backup"}
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in ignored_parts for part in path.parts):
            continue
        if path.suffix.lower() in suffixes:
            files.append(path)
    return sorted(files)


def check_portable_paths(results: list[CheckResult]) -> None:
    patterns = [
        re.compile(r"[A-Za-z]:\\Users\\"),
        re.compile(r"[A-Za-z]:/Users/"),
        re.compile(r"\\Documents\\杂务"),
        re.compile(r"/Documents/杂务"),
    ]
    hits: list[str] = []
    for path in iter_text_files():
        rel = str(path.relative_to(ROOT)).replace("\\", "/")
        content = read_text(path)
        for pattern in patterns:
            if pattern.search(content):
                hits.append(rel)
                break
    if hits:
        add(results, "FAIL", "可移植路径检查", f"发现本机绝对路径残留: {', '.join(hits)}")
    else:
        add(results, "PASS", "可移植路径检查", "未发现常见本机绝对路径残留。")


def check_line_budget(results: list[CheckResult], rel_path: str, soft_limit: int) -> None:
    path = ROOT / rel_path
    if not path.exists():
        add(results, "FAIL", f"体量: {rel_path}", "文件不存在，无法判断。")
        return
    count = len(read_text(path).splitlines())
    if count <= soft_limit:
        add(results, "PASS", f"体量: {rel_path}", f"{count} 行，仍在轻量范围内。")
    elif count <= soft_limit + 30:
        add(results, "WARN", f"体量: {rel_path}", f"{count} 行，接近膨胀边界。")
    else:
        add(results, "FAIL", f"体量: {rel_path}", f"{count} 行，建议收缩顶层内容。")


def check_context_budget(results: list[CheckResult]) -> None:
    hot_paths = [
        ROOT / "AGENTS.md",
        ROOT / "PROJECT-WORKFLOW.md",
        ROOT / ".project-memory" / "README.md",
        ROOT / ".project-memory" / "tool-delivery-routing.md",
        ROOT / ".project-memory" / "plugin-mcp-governance.md",
        ROOT / ".project-memory" / "capability-fallback-matrix.md",
        ROOT / ".project-memory" / "text-selector-questioning-protocol.md",
    ]
    missing = [str(path.relative_to(ROOT)).replace("\\", "/") for path in hot_paths if not path.exists()]
    if missing:
        add(results, "FAIL", "误广加载预算", f"缺少文件，无法评估: {', '.join(missing)}")
        return
    estimate = sum(approx_token_count(read_text(path)) for path in hot_paths)
    if estimate <= 12000:
        add(results, "PASS", "误广加载预算", f"约 {estimate} tokens。")
    elif estimate <= 14000:
        add(results, "WARN", "误广加载预算", f"约 {estimate} tokens，接近预算上限。")
    else:
        add(results, "FAIL", "误广加载预算", f"约 {estimate} tokens，已超过预算上限。")


def summarize(results: list[CheckResult]) -> tuple[int, int]:
    fail_count = sum(1 for result in results if result.level == "FAIL")
    warn_count = sum(1 for result in results if result.level == "WARN")
    return fail_count, warn_count


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    results: list[CheckResult] = []

    required_paths = [
        "AGENTS.md",
        "PROJECT-WORKFLOW.md",
        ".project-memory",
        ".project-memory/README.md",
        ".project-memory/automation-entrypoints.md",
        ".project-memory/plugin-mcp-governance.md",
        ".project-memory/capability-registry.md",
        ".project-memory/capability-fallback-matrix.md",
        ".project-memory/weekly-maintenance-report-template.md",
        ".project-memory/rule-deletion-guidelines.md",
        ".project-memory/memory-write-thresholds.md",
        ".project-memory/memory-retention-and-expiry.md",
        ".project-memory/memory-audit-playbook.md",
        ".project-memory/document-condense-template.md",
        ".project-memory/expansion-budget-policy.md",
        ".project-memory/text-selector-questioning-protocol.md",
        ".project-memory/tool-delivery-routing.md",
        ".project-memory/validation-pre-delivery.md",
        ".project-memory/validation-harness-health.md",
        ".project-memory/knowledge-cache/index.md",
        "harness-regression/README.md",
        "harness-regression/cases",
        "harness-regression/drills/README.md",
        "harness-regression/drills/memory/README.md",
        "tools/check_harness.py",
        "tools/auto_cold_layer_maintenance.py",
        "install.ps1",
        "install.cmd",
    ]
    for rel_path in required_paths:
        check_exists(results, rel_path)

    for rel_path in [
        "harness-regression/cases/01-review-notes.md",
        "harness-regression/cases/02-essay-outline.md",
        "harness-regression/cases/03-presentation-delivery.md",
        "harness-regression/cases/04-document-condense.md",
        "harness-regression/cases/05-click-option-questioning.md",
    ]:
        check_contains(
            results,
            rel_path,
            ["## 用户请求", "## 期望路由", "## 最低合格输出", "## 常见跑偏"],
            f"回归样例: {rel_path}",
        )

    check_portable_paths(results)
    check_line_budget(results, "AGENTS.md", 170)
    check_line_budget(results, "PROJECT-WORKFLOW.md", 140)
    check_context_budget(results)

    fail_count, warn_count = summarize(results)

    print("Harness Health Check")
    print(f"Root: {ROOT}")
    print()
    for result in results:
        print(f"[{result.level}] {result.name}")
        print(f"  {result.detail}")

    print()
    if fail_count == 0 and warn_count == 0:
        print("结论: PASS")
        print("当前 package 结构完整，路径可移植，基础样例可用。")
        return 0

    if fail_count == 0:
        print("结论: PASS WITH WARNINGS")
        print(f"存在 {warn_count} 个警告，建议继续收缩或补齐。")
        return 0

    print("结论: FAIL")
    print(f"存在 {fail_count} 个失败项，建议先修复再继续扩展。")
    return 1


if __name__ == "__main__":
    sys.exit(main())
