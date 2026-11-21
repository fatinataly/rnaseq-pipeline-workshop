# Scripts

Shell scripts for the command-line steps. Each script should read its settings from `../config/config.yaml` or take arguments, never hard-coded paths.

Planned:

- `01_download.sh`: download FASTQ files from SRA
- `02_qc.sh`: FastQC, fastp and MultiQC
- `03_salmon.sh`: build the index and quantify each sample
