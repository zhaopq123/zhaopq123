#!/usr/bin/env python3
"""同步 GitHub 个人主页的项目表（zhaopq123/zhaopq123 仓库）。

用法：
    python sync_profile.py            # 检查并同步（有变化才提交推送）
    python sync_profile.py --check    # 只检查不写入

每次开源新项目后只需两步：
    1. 在 projects_meta.json 里加一条 {name: {tagline, tech}}
    2. 跑本脚本

新开源了项目但忘了加 meta 也不会漏——脚本会对比 GitHub 实际公开仓库，
发现缺的就自动用 description 兜底加进表里，并打印提醒。
"""

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
README = HERE / "README.md"
META = HERE / "projects_meta.json"
PROXY = "http://127.0.0.1:7897"
# 不进项目表的仓库（个人主页自身等）
EXCLUDE = {"zhaopq123"}

# 代理与直连都会变，别赌单边：2026-10-15 白天实测 github.com:443 被 reset、
# 代理 7897 已停，api.github.com 直连照样通（所以读取一律直连，代理挂了也能 --check）；
# 同日稍晚直连完全恢复，push 直连成功。因此 push = 直连优先、失败回退代理，两条路都留。
GH_ENV = {**os.environ, "HTTPS_PROXY": PROXY, "HTTP_PROXY": PROXY}
# 读取用：显式剥掉代理变量，避免继承到一个已经停掉的端口上（那种失败长得像网络问题）
DIRECT_ENV = {
    k: v
    for k, v in os.environ.items()
    if k.lower() not in ("http_proxy", "https_proxy", "all_proxy")
}


def gh(*args: str, use_proxy: bool = False) -> str:
    r = subprocess.run(
        ["gh", *args],
        env=GH_ENV if use_proxy else DIRECT_ENV,
        capture_output=True,
        text=True,
        # gh 输出恒为 UTF-8；Windows 默认按 GBK 解码会在仓库 description 含中文时
        # 直接把输出吞成 None（2026-10-17 实测）。显式指定编码，跨平台一致。
        encoding="utf-8",
        errors="replace",
        timeout=120,
    )
    if r.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args)} 失败: {r.stderr.strip()[:300]}")
    return r.stdout


def load_meta() -> dict:
    if META.exists():
        return json.loads(META.read_text(encoding="utf-8"))
    return {}


def fetch_repos() -> tuple[list[dict], list[str]]:
    """返回 (可上表的仓库, 被私有过滤掉的仓库名)。

    项目表是公开主页上的，链接必须点得开。`GET /users/{login}/repos` 在不同令牌
    范围下会不会把私有仓也带回来并不稳定（2026-10-14 那次就把当时列到、事后核验
    实为私有的 diagram-design 渲上了表，访客点开是 404），所以这里按 `private`
    字段硬过滤，不依赖端点行为。
    """
    out = gh("api", "users/zhaopq123/repos?per_page=100&sort=updated")
    skipped, repos = [], []
    for r in json.loads(out):
        if r.get("name") in EXCLUDE or r.get("fork") or r.get("archived"):
            continue
        if r.get("private"):
            skipped.append(r["name"])
            continue
        repos.append(r)
    return repos, skipped


def render_table(repos: list[dict], meta: dict) -> tuple[str, list[str]]:
    """返回 (表格 markdown, 需要人工补充 meta 的项目名列表)。"""
    rows, need_meta = [], []
    seen = set()
    # meta 里声明的优先（保持人工排的顺序）
    for name, info in meta.items():
        repo = next((r for r in repos if r["name"] == name), None)
        if not repo:
            continue  # meta 里有但 GitHub 上没有（比如还没创建），跳过
        url = repo["html_url"]
        desc = repo.get("description") or ""
        tagline = info.get("tagline") or desc.split("：")[0].split(" — ")[0] or name
        tech = info.get("tech") or "—"
        rows.append(f"| **[{name}]({url})** | {tagline} | {tech} |")
        seen.add(name)
    # GitHub 上有、meta 里没有的 → 用 description 兜底，提醒补
    for r in repos:
        name = r["name"]
        if name in seen:
            continue
        desc = (r.get("description") or "").strip() or "（待补充简介）"
        rows.append(f"| **[{name}]({r['html_url']})** | {desc} | — |")
        need_meta.append(name)
    if not rows:
        return "（暂无公开项目）", []
    header = "| 项目 | 一句话 | 技术点 |\n|---|---|---|"
    return header + "\n" + "\n".join(rows), need_meta


def replace_section(readme: str, table: str) -> str:
    start = "<!-- SYNC:PROJECTS:START -->"
    end = "<!-- SYNC:PROJECTS:END -->"
    i, j = readme.find(start), readme.find(end)
    if i < 0 or j < 0:
        raise RuntimeError("README 里找不到 SYNC 标记，请检查 README.md")
    # 保留标记本身，否则下次同步找不到 START
    return readme[:i] + start + "\n" + table + "\n\n" + readme[j:]


def main() -> int:
    check_only = "--check" in sys.argv
    meta = load_meta()
    repos, skipped = fetch_repos()
    table, need_meta = render_table(repos, meta)

    print(f"GitHub 可上表仓库 {len(repos)} 个，meta 声明 {len(meta)} 个")
    if skipped:
        print(f"\n🔒 私有仓不进公开项目表（链接会 404）: {', '.join(skipped)}")
        print("   要上表就先把该仓设成公开，别手改 README。")
    if need_meta:
        print("\n⚠️ 以下项目缺 meta（已用 description 兜底，建议补充）:")
        for n in need_meta:
            print(f"   - {n}")

    readme = README.read_text(encoding="utf-8")
    new = replace_section(readme, table)
    if new == readme:
        print("\n✓ 无变化")
        return 0
    if check_only:
        print("\n⚠️ 有变化（--check 未写入）")
        return 1

    README.write_text(new, encoding="utf-8")
    subprocess.run(["git", "add", "README.md"], cwd=HERE, check=True)
    names = ", ".join(r["name"] for r in repos)
    msg = (
        "docs: sync 项目表（"
        + datetime.now().strftime("%Y-%m-%d")
        + f"）\n\n当前公开项目: {names}"
    )
    subprocess.run(["git", "commit", "-m", msg], cwd=HERE, check=True)
    # push：直连优先（网络正常时最快），失败再走代理兜底（被墙时的老路）
    p = subprocess.run(["git", "push", "origin", "main"], cwd=HERE, env=DIRECT_ENV)
    if p.returncode != 0:
        print("直连 push 失败，改用代理重试…")
        subprocess.run(["git", "push", "origin", "main"], cwd=HERE, env=GH_ENV, check=True)
    print("\n✓ 已同步并推送")
    return 0


if __name__ == "__main__":
    sys.exit(main())
