python scripts/fairy_commit.py && \
  if git status --porcelain CHANGELOG.md | grep -q .; then \
    git add CHANGELOG.md && \
    git commit -m "🧚 fairy dust: update CHANGELOG from fairy notes" && \
    git push; \
  else \
    echo "No new fairy notes."; \
  fi
