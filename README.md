# RNA-seq Pipeline Workshop

[![CI](https://github.com/MultiOmics-Intelligence/rnaseq-pipeline-workshop/actions/workflows/ci.yml/badge.svg)](https://github.com/MultiOmics-Intelligence/rnaseq-pipeline-workshop/actions/workflows/ci.yml)

A hands-on **group project** at MultiOmics Intelligence. Two teams each analyse a real bulk RNA-seq dataset step by step in Python, from raw reads to biological interpretation, while learning good coding practice, GitHub and Agile with Jira.

The workshop was proposed and is led by **Fatima Diaz** ([@fatinataly](https://github.com/fatinataly)).

---

## 🎯 Goals
- Walk through a classical RNA-seq pipeline: data preparation → quality control → quantification → differential expression → functional interpretation.
- Practise Python best practices: project structure, virtual environments, testing, linting and documentation.
- Work as a team using **GitHub** (branches, pull requests, code review) and **Jira** (Agile, weekly sprints).
- Welcome all experience levels: tasks are labelled `beginner`, `intermediate` or `advanced`.

## 👥 How the group project works
- Participants are split into **two groups, Group A and Group B**. Members will be announced.
- Both groups follow **the same pipeline, the same folder structure and the same plan**, but each works on **its own dataset**.
- Work is planned in **weekly sprints** in Jira. Each ticket belongs to one group and has a difficulty level.
- At the end, each group presents its results, and together we compare the two analyses: what worked the same, what had to change, and why.

The step-by-step plan is in [`docs/workshop-plan.md`](docs/workshop-plan.md).

## 🧬 Datasets

| Group | Dataset | Design | Status |
|-------|---------|--------|--------|
| Group A | to be decided | to be decided | ⏳ Pending |
| Group B | to be decided | to be decided | ⏳ Pending |

A good workshop dataset has:
- raw FASTQ files on SRA **and** a published count matrix (useful as a check, or as a fallback);
- a simple two-condition design with at least 3 replicates per condition;
- a small number of samples (about 6–12) so that it runs on a laptop;
- a well-annotated organism (human or mouse) and a clear paper to compare with.

Already proposed: **Himes et al. 2014 (GEO: GSE52778)**, human airway smooth muscle cells treated with dexamethasone vs. untreated. It is small, well documented and widely used for teaching.

## 🔬 Pipeline overview

| # | Step | Tools | Main output |
|---|------|-------|-------------|
| 1 | Data download & metadata | SRA Toolkit, pandas | FASTQ files, `samples.csv` |
| 2 | Quality control & trimming | FastQC, MultiQC, fastp | MultiQC report, trimmed reads |
| 3 | Quantification | Salmon, pytximport | Gene count matrix |
| 4 | Exploratory analysis | pandas, scikit-learn (PCA), seaborn | PCA and sample-distance plots |
| 5 | Differential expression | PyDESeq2 | DE results table, MA and volcano plots |
| 6 | Functional enrichment | gseapy | Enriched pathways |
| 7 | Biological interpretation | matplotlib, seaborn | Final figures and key messages |

Each step has a notebook with the same number in each group's `notebooks/` folder.

## 📁 Project structure

```
rnaseq-pipeline-workshop/
├── README.md
├── CONTRIBUTING.md          # GitHub + Jira workflow
├── environment.yml          # conda environment for everyone
├── pyproject.toml           # shared package + lint/test settings
├── docs/
│   └── workshop-plan.md     # sprints, deliverables, definition of done
├── src/rnaseq_workshop/     # shared code used by both groups
├── tests/                   # tests for the shared code
├── groups/
│   ├── group-a/
│   │   ├── config/config.yaml   # dataset, design, thresholds
│   │   ├── data/                # metadata committed; raw/processed ignored
│   │   ├── scripts/             # shell scripts (download, QC, Salmon)
│   │   ├── notebooks/           # 01_… to 07_…, one per step
│   │   └── results/             # figures/ and tables/
│   └── group-b/                 # same layout as group-a
└── .github/                 # CI, pull request and issue templates
```

**Rules of thumb**
- Work only inside **your group's folder**. Changes to `src/`, `tests/` or `docs/` are shared and need a review from someone in each group.
- **Never commit data** (FASTQ, BAM, Salmon output, count matrices). `.gitignore` already blocks them.
- Settings live in `config/config.yaml`, not in the notebooks.

## 🚀 Getting started

### Option A: Workshop participants (with write access)

```bash
git clone https://github.com/MultiOmics-Intelligence/rnaseq-pipeline-workshop.git
cd rnaseq-pipeline-workshop
conda env create -f environment.yml
conda activate rnaseq-workshop
```

Then go to your group's folder (`groups/group-a` or `groups/group-b`), create a branch, commit your changes, push the branch and open a Pull Request to `main`.

### Option B: External contributors (without write access)
1. Click **Fork** at the top right of this page.
2. Clone your fork:

```bash
git clone https://github.com/<your-username>/rnaseq-pipeline-workshop.git
cd rnaseq-pipeline-workshop
conda env create -f environment.yml
conda activate rnaseq-workshop
```

3. Create a branch, commit your changes and push them to your fork.
4. Open a Pull Request to `MultiOmics-Intelligence/rnaseq-pipeline-workshop`.

> 💡 Before starting new work, click **Sync fork** on your fork's GitHub page to get the latest changes.

### Check your setup

```bash
ruff check .
pytest
```

## 🤝 Contributing
1. Pick a ticket from your group's current Jira sprint.
2. Create a branch: `feature/<JIRA-KEY>-short-description` (for example `feature/RNA-12-fastqc-report`).
3. Open a Pull Request, fill in the template and request at least one review.
4. Merge after review and passing CI.

Full details are in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## 📬 Contact
- **Workshop lead:** Fatima Diaz, [@fatinataly](https://github.com/fatinataly)
- **Organisation:** [MultiOmics Intelligence](https://multiomicsintelligence.co.uk)

Questions about a task are best asked in the Jira ticket or the pull request, so the whole group can see the answer.

## 📜 License
MIT, see [`LICENSE`](LICENSE).
