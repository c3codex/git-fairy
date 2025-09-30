#!/usr/bin/env python3
from __future__ import annotations
import os, re, datetime, pathlib

ROOT = pathlib.Path(".").resolve()
CHANGELOG = ROOT / "CHANGELOG.md"

# files the fairy will scan
INCLUDE_EXT = {".md", ".mdx", ".txt", ".yaml", ".yml", ".json"}

# a line counts as a fairy note if it contains "fairy:" (case-insensitive)
FAIRY_PATTERN = re.compile(r"fairy\s*:", re.IGNORECASE)

def find_repo_notes() -> dict[str, list[str]]:
    notes: dict[str, list[str]] = {}
    for path in ROOT.rglob("*"):
        if not path.is_file(): 
            continue
        if path.parts and path.parts[0] in {".git", ".github"}:
            # skip .git and workflow internals (no recursion into .github/templates if you want that included, remove this)
            pass
        ext = path.suffix.lower()
        if ext not in INCLUDE_EXT:
            continue
        try:
            with path.open("r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
        except Exception:
            continue
        hits = []
        for i, line in enumerate(lines, start=1):
            if FAIRY_PATTERN.search(line):
                clean = line.strip()
                hits.append(f"L{i}: {clean}")
        if hits:
            rel = str(path.relative_to(ROOT))
            notes[rel] = hits
    return notes

def ensure_changelog_exists():
    if not CHANGELOG.exists():
        CHANGELOG.write_text("# CHANGELOG\n\n", encoding="utf-8")

def append_to_changelog(collected: dict[str, list[str]]):
    today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    section_header = f"## {today} — Fairy Sweep\n\n"
    # if today's section already exists, we append beneath it
    existing = CHANGELOG.read_text(encoding="utf-8")
    insertion = []
    if section_header not in existing:
        insertion.append(section_header)
    for file, lines in sorted(collected.items()):
        insertion.append(f"- **{file}**")
        for l in lines:
            # de-emphasize the literal "fairy:" in the log
            pretty = re.sub(FAIRY_PATTERN, "**fairy:**", l)
            insertion.append(f"  - {pretty}")
        insertion.append("")  # blank line
    if insertion:
        with CHANGELOG.open("a", encoding="utf-8") as f:
            f.write("\n".join(insertion))

def main():
    ensure_changelog_exists()
    collected = find_repo_notes()
    if not collected:
        print("No fairy notes found.")
        return
    append_to_changelog(collected)
    print(f"Appended notes for {len(collected)} file(s) to CHANGELOG.md")

if __name__ == "__main__":
    main()
