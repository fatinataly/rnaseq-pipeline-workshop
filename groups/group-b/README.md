# Group B

**Members:** to be announced
**Dataset:** to be decided (see [`config/config.yaml`](config/config.yaml))

## Folder layout

| Folder | What goes here |
|--------|----------------|
| `config/` | `config.yaml`: dataset, paths, design and thresholds used by every notebook |
| `data/metadata/` | `samples.csv` (small, committed) |
| `data/raw/`, `data/processed/` | FASTQ, Salmon output, count matrices (**not committed**, ignored by git) |
| `scripts/` | Shell scripts for the command-line steps (download, QC, Salmon) |
| `notebooks/` | One notebook per pipeline step, run in order |
| `results/figures/`, `results/tables/` | Final figures and tables for the presentation |

## Progress

| Step | Notebook | Status |
|------|----------|--------|
| 1. Data download and metadata | `01_data_download_and_metadata.ipynb` | Not started |
| 2. Quality control and trimming | `02_quality_control.ipynb` | Not started |
| 3. Quantification | `03_quantification.ipynb` | Not started |
| 4. Exploratory analysis | `04_exploratory_analysis.ipynb` | Not started |
| 5. Differential expression | `05_differential_expression.ipynb` | Not started |
| 6. Functional enrichment | `06_functional_enrichment.ipynb` | Not started |
| 7. Biological interpretation | `07_biological_interpretation.ipynb` | Not started |
