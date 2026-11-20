# Contributing

This is how we work together on GitHub and Jira during the workshop.

## 1. Jira: plan the work
- Each group has its own **weekly sprint**.
- Every ticket has:
  - a **group** label: `group-a`, `group-b` or `shared`;
  - a **level** label: `beginner`, `intermediate` or `advanced`;
  - a clear **"done when"** description.
- Move your ticket to *In Progress* when you start and to *In Review* when you open the pull request.

## 2. Git: one branch per ticket

```bash
git checkout main
git pull
git checkout -b feature/<JIRA-KEY>-short-description
```

- Use `fix/<JIRA-KEY>-…` for bug fixes and `docs/<JIRA-KEY>-…` for documentation only.
- Commit small, focused changes with clear messages, for example `RNA-12: add MultiQC summary to QC notebook`.
- Never commit to `main` directly.

## 3. Pull requests
- Open a pull request to `main` and fill in the template.
- Put the Jira key in the title, for example `RNA-12: FastQC report for Group A`.
- Request **at least one reviewer** from your group. Changes to `src/`, `tests/` or `docs/` need a reviewer from **each** group.
- CI (lint and tests) must pass before merging.
- The author merges after approval, then deletes the branch.

## 4. Reviewing
- Be kind and specific: suggest, explain why, and point to the line.
- Check that the notebook runs from top to bottom and that the markdown explains each step.
- Approve when it is good enough to build on; it does not have to be perfect.

## 5. Code style
- Read settings from `config/config.yaml`; do not hard-code paths, sample names or thresholds.
- Put code that both groups need in `src/rnaseq_workshop/`, with a test in `tests/`.
- Before pushing, run:

```bash
ruff check .
pytest
```

## 6. Data
- Never commit FASTQ, BAM, Salmon output or count matrices. They stay in `data/raw/` and `data/processed/`, which git ignores.
- `data/metadata/samples.csv` is small and **should** be committed.
