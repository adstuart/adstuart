#!/usr/bin/env python3
"""Update the generated public repository section in the profile README."""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import textwrap
import urllib.error
import urllib.request


OWNER = os.getenv("GITHUB_OWNER", "adstuart")
README_PATH = os.getenv("README_PATH", "README.md")
START = "<!-- PUBLIC-REPOS:START -->"
END = "<!-- PUBLIC-REPOS:END -->"
ACTIVE_CUTOFF = dt.datetime(2025, 1, 1, tzinfo=dt.timezone.utc)

AI_KEYWORDS = {
    "ai",
    "agentic",
    "copilot",
    "foundry",
    "ai-gateway",
    "mcp",
    "model",
    "llm",
    "video-factory",
}

NETWORKING_KEYWORDS = {
    "appgateway",
    "arc-esu",
    "ars",
    "azfw",
    "dns",
    "dnat",
    "ecmp",
    "ergw",
    "expressroute",
    "firewall",
    "floatingip",
    "gwlb",
    "infoblox",
    "load-balancer",
    "network",
    "networking",
    "p2s",
    "privatelink",
    "private-link",
    "routeserver",
    "sdwan",
    "s2s",
    "subnet",
    "vpn",
    "vtap",
    "vwan",
    "vnet",
}

TOOLING_KEYWORDS = {
    "cli",
    "compared",
    "cost",
    "docs",
    "factory",
    "goal",
    "latency",
    "meter",
    "teams",
    "watch",
}

TOOLING_OVERRIDES = {
    "azure-storage-local-arc",
    "cloud-networking-compared",
}


def github_json(url: str) -> list[dict]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": f"{OWNER}-profile-readme-updater",
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    repos: list[dict] = []
    page = 1
    while True:
        request = urllib.request.Request(f"{url}&page={page}", headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                batch = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"GitHub API failed: {exc.code} {detail}") from exc

        if not batch:
            return repos
        repos.extend(batch)
        page += 1


def parse_timestamp(value: str | None) -> dt.datetime:
    if not value:
        return dt.datetime(1970, 1, 1, tzinfo=dt.timezone.utc)
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def words(repo: dict) -> set[str]:
    raw = " ".join(
        str(part or "")
        for part in (
            repo.get("name"),
            repo.get("description"),
        )
    ).lower()
    return set(re.findall(r"[a-z0-9]+", raw))


def has_any(repo: dict, keywords: set[str]) -> bool:
    repo_words = words(repo)
    name = str(repo.get("name", "")).lower()
    description = str(repo.get("description", "") or "").lower()
    phrase_keywords = {k for k in keywords if "-" in k}
    return bool(repo_words & keywords) or any(
        k in name or k in description for k in phrase_keywords
    )


def categorize(repo: dict) -> str:
    name = repo["name"]
    if name == OWNER:
        return "skip"
    if repo.get("fork"):
        return "skip"

    if has_any(repo, AI_KEYWORDS):
        return "AI and agents"

    if name in TOOLING_OVERRIDES:
        return "Tools, demos, and experiments"

    if has_any(repo, NETWORKING_KEYWORDS) or name.startswith("azure-"):
        pushed_at = parse_timestamp(repo.get("pushed_at"))
        if repo.get("archived") or pushed_at < ACTIVE_CUTOFF:
            return "Azure networking - older or archived"
        return "Azure networking - active"

    if has_any(repo, TOOLING_KEYWORDS):
        return "Tools, demos, and experiments"

    return "Other public repos"


def clean_description(text: str | None) -> str:
    if not text:
        return ""
    normalized = " ".join(text.split())
    return textwrap.shorten(normalized, width=110, placeholder="...")


def render_repo(repo: dict) -> str:
    description = clean_description(repo.get("description"))
    suffix = " _(archived)_" if repo.get("archived") else ""
    if not description:
        return f"- [{repo['name']}]({repo['html_url']}){suffix}"
    return f"- [{repo['name']}]({repo['html_url']}) — {description}{suffix}"


def render_section(repos: list[dict]) -> str:
    categories = {
        "AI and agents": [],
        "Azure networking - active": [],
        "Azure networking - older or archived": [],
        "Tools, demos, and experiments": [],
        "Other public repos": [],
    }

    for repo in repos:
        category = categorize(repo)
        if category != "skip":
            categories[category].append(repo)

    latest_activity = max(
        (parse_timestamp(repo.get("pushed_at")) for repo in repos),
        default=dt.datetime(1970, 1, 1, tzinfo=dt.timezone.utc),
    ).strftime("%Y-%m-%d")
    lines = [f"_Generated from public GitHub repo metadata. Latest activity: {latest_activity}._", ""]

    for category, items in categories.items():
        items.sort(key=lambda item: parse_timestamp(item.get("pushed_at")), reverse=True)
        if not items:
            continue
        lines.append(f"<details>")
        lines.append(f"<summary><strong>{category}</strong> ({len(items)})</summary>")
        lines.append("")
        lines.extend(render_repo(item) for item in items)
        lines.append("")
        lines.append("</details>")
        lines.append("")

    return "\n".join(lines).rstrip()


def main() -> int:
    repos = github_json(
        f"https://api.github.com/users/{OWNER}/repos?per_page=100&type=owner&sort=pushed"
    )
    readme = open(README_PATH, encoding="utf-8").read()
    if START not in readme or END not in readme:
        raise RuntimeError(f"README must contain {START} and {END} markers")

    generated = render_section(repos)
    updated = re.sub(
        rf"{re.escape(START)}.*?{re.escape(END)}",
        f"{START}\n{generated}\n{END}",
        readme,
        flags=re.DOTALL,
    )
    with open(README_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(updated)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

