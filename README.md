# Deadline-Aware Explainable NIDS Reproducibility Package

This repository contains the frozen artifacts, evaluation notebooks, manifests, and result files supporting the study on deadline-aware explainable network intrusion detection.

## Scope

The primary CSE-CIC-IDS2018 experiment is a binary benchmark limited to Benign, FTP-BruteForce, and SSH-Bruteforce traffic. It is not a comprehensive evaluation of all attack families in CSE-CIC-IDS2018. The repository preserves the reported detector, TreeSHAP faithfulness, constrained explanation, and latency evidence.

## Repository structure

- `integrity/`: feature and split manifests, checksums, and verification report.
- `models/`: frozen scikit-learn and ONNX detector artifacts.
- `detection/`: baseline, port-ablation, five-seed, and frozen-test notebooks and outputs.
- `explainability/`: TreeSHAP faithfulness and constrained explanation notebooks and outputs.
- `latency/`: ONNX detector and end-to-end latency notebooks and timing outputs.
- `unsw/`: published UNSW-NB15 operating-point summaries and a script that independently recomputes the paired threshold trade-off from the reported discordant counts.

## Dataset

The original CSE-CIC-IDS2018 files are not redistributed here. Obtain the dataset from its official source and reproduce the preprocessing/splitting procedure described in the notebooks and manifests. The published derived predictions and evaluation outputs allow independent verification of the reported metrics without redistributing the source dataset.

## Reproduction notes

1. Create a Python environment using `requirements.txt`.
2. Download and preprocess the required CSE-CIC-IDS2018 subsets.
3. Update `PROJECT_DIR` in the notebooks to your local project directory.
4. Run the notebooks in numerical order within each study component.
5. Verify artifact hashes using `integrity/SHA256SUMS.txt` where applicable.

The notebooks preserve their recorded outputs to document the reported execution. Absolute Google Drive paths reflect the original experiment environment and must be changed for a new environment.

## Reproducibility boundary

Hardware-dependent latency values should be remeasured on the target system. The manifests record the software/runtime settings available from the original runs; the original detector CPU model and RAM capacity were not captured and are therefore not inferred here.

The UNSW-NB15 release is currently a summary-level verification package. It does not include row-level holdout predictions or the original benchmark rows. This boundary is stated in `unsw/README.md`.

## Citation

Please cite the associated manuscript when using these artifacts. The final bibliographic citation will be added after publication.
