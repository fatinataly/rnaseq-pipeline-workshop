# rnaseq-pipeline-workshop

A hands-on workshop where we analyse a real bulk RNA-seq dataset step by step, from raw reads to biological interpretation, using Python.

## 🎯 Goals
- Walk through a classical RNA-seq pipeline: data preparation → quality control → quantification → differential expression → functional interpretation.
- Practise Python best practices: project structure, virtual environments, testing, linting and documentation.
- Work as a team using **GitHub** (branches, pull requests, code review) and **Jira** (Agile, weekly sprints).
- Accommodate all experience levels: tasks are labelled `beginner`, `intermediate` or `advanced`.

## 🧬 Dataset
Proposed: **Himes et al. 2014 (GEO: GSE52778)**, human airway smooth muscle cells treated with dexamethasone vs. untreated. It's small, well documented and widely used for teaching.

## 🔬 Pipeline overview
| Step | Tools |
|------|-------|
| Data download & metadata | SRA Toolkit, pandas |
| Quality control & trimming | FastQC, MultiQC, fastp |
| Quantification | Salmon, pytximport |
| Exploratory analysis | pandas, scikit-learn (PCA), seaborn |
| Differential expression | PyDESeq2 |
| Functional enrichment | gseapy |

## 📁 Project structure (TODO — IN PROGRESS)

## 🚀 Getting started
```bash
git clone https://github.com/fatinataly/rnaseq-pipeline-workshop.git
cd rnaseq-pipeline-workshop
conda env create -f environment.yml
conda activate rnaseq-workshop
```

## 🤝 Contributing
1. Pick a ticket from the current Jira sprint.
2. Create a branch: `feature/<JIRA-KEY>-short-description`.
3. Open a Pull Request and request at least one review.
4. Merge after review and passing CI.

## 📬 Contact

If you want to talk science, collaborate, or just commiserate about
read quality filtering — find me here:

- 😺 **GitHub:** [fatinataly](https://github.com/fatinataly)
- 💼 **LinkedIn:** [Fatima Diaz](https://www.linkedin.com/in/fátima-ddiaz/)
- 📧 **Email:** fatinataly@gmail.com


## 📜 License
MIT
