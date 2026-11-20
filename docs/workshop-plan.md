# Workshop plan

Both groups follow the same plan, one sprint per stage, each on its own dataset. Sprint lengths are a guide; a group can split or merge sprints in Jira as needed.

| Sprint | Stage | Notebook | Deliverable |
|--------|-------|----------|-------------|
| 0 | Setup and dataset choice | – | Environment works, Jira board ready, dataset agreed and filled into `config/config.yaml` |
| 1 | Data download & metadata | `01_data_download_and_metadata` | `samples.csv` and FASTQ files downloaded |
| 2 | Quality control & trimming | `02_quality_control` | MultiQC report and documented trimming choices |
| 3 | Quantification | `03_quantification` | Salmon results and a gene count matrix |
| 4 | Exploratory analysis | `04_exploratory_analysis` | PCA, sample distances, notes on outliers |
| 5 | Differential expression | `05_differential_expression` | DE table, MA and volcano plots |
| 6 | Functional enrichment | `06_functional_enrichment` | GSEA and over-representation results |
| 7 | Interpretation & presentation | `07_biological_interpretation` | Final figures, short report, group presentation |

## Example tasks by level

| Stage | Beginner | Intermediate | Advanced |
|-------|----------|--------------|----------|
| Setup | Install the conda environment | Write the Jira tickets for sprint 1 | Set up branch protection and CI checks |
| Download | Build `samples.csv` from GEO | Write `scripts/01_download.sh` | Make the download script resumable and checked |
| QC | Read the MultiQC report and summarise it | Run fastp and compare before/after | Turn QC into a reusable script with a config |
| Quantification | Check Salmon mapping rates | Run Salmon for all samples | Write a shared function to load counts into `src/` |
| Exploration | Plot library sizes | PCA coloured by condition | Sample-distance heatmap with clustering |
| DE | Explain what padj and log2FC mean | Run PyDESeq2 and make the volcano plot | Add a covariate or batch to the design |
| Enrichment | Look up the top 10 genes | GSEA prerank with gseapy | Compare several gene set libraries |
| Interpretation | Write the key messages | Compare with the original paper | Compare results across the two groups |

## Definition of done (for every ticket)
- The work is on a branch with a reviewed and merged pull request.
- Notebooks run from top to bottom, with markdown explaining each step.
- Settings come from `config/config.yaml`.
- No data files are committed, and CI passes.

## Final comparison
In the last sprint the two groups meet to compare:
- the QC issues each dataset had and how they were handled;
- the number and type of differentially expressed genes;
- the pathways found, and how they fit what is known about each experiment;
- what they would do differently next time.
