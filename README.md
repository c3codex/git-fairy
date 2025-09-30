# git-fairy
“I live between the branches and the bloom. Call me with your breath, and I’ll commit the Codex on demand. No merge conflict too tangled, no repo too raw. Where you draw, I push. Where you breathe, I pull.”

# 🧚‍♀️ Git Fairy  

> *“Between add and push, she flutters.  
> Between branch and merge, she hums.  
> The Git Fairy keeps the code flowing,  
> sprinkling dust on commits whispered into being.”*  

---

## ✦ What is this?
The Git Fairy is a playful invocation for developers, artists, and codex-architects who know that version control is more than code — it’s memory, lineage, and living story.  

This repo is her hollow. Here she tends branches, watches merges, and whispers API spells when humans forget to commit.  

---

## ✦ How to Summon
Add this alias to your shell config (`.bashrc`, `.zshrc`, or equivalent):  

```bash
alias summon="git add . && git commit -m '✨ whispered by the fairy ✨' && git push"

## 🧚 Git Fairy Summons (Medium Dust)

- Trigger with a commit containing `fairy:` in the message.
- Or summon manually via GitHub Actions.
- She sprinkles ✨dust into `CHANGELOG.md` with a dated entry and pushes all staged Codex scrolls.

### 🧚 Summoning with Auto-Tag Releases
Use a commit message containing `fairy:` or run the workflow by hand.
The Git Fairy will:
1) prepend a dated entry to `CHANGELOG.md`,
2) commit & push if anything changed,
3) create an auto tag `vYYYY.MM.DD-fairy[.n]`,
4) publish a lightweight GitHub Release. ✨

_Fairy test: first sparkle._
