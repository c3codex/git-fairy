#!/usr/bin/env python3
import os
import re
from datetime import datetime

# Path to your CHANGELOG
changelog = "docs/CHANGELOG.md"

def find_fairy_notes():
    notes = []
    for root, _, files in os.walk("."):
        for f in files:
            if f.endswith((".py", ".md", ".yml", ".yaml")):
                path = os.path.join(root, f)
                try:
                    with open(path, "r", encoding="utf-8") as fh:
                        for line in fh:
                            if "# fairy:" in line.lower():
                                notes.append(f"- {path}: {line.strip()}")
                except Exception:
                    pass
    return notes

def update_changelog(notes):
    if not notes:
        return
    header = f"\n## Fairy Sweep {datetime.utcnow().isoformat()} UTC\n"
    entry = header + "\n".join(notes) + "\n"
    with open(changelog, "a", encoding="utf-8") as fh:
        fh.write(entry)

if __name__ == "__main__":
    notes = find_fairy_notes()
    update_changelog(notes)
    if notes:
        print("✨ Fairy dusted notes into CHANGELOG")
    else:
        print("✨ Fairy found no notes this pass")
