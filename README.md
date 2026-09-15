<div align="center">

# TRACE & TCFN for Photovoltaic Power Forecasting

**Data and executable notebooks for reproducing the forecasting workflow described in the paper**

[![Python 3.9](https://img.shields.io/badge/Python-3.9.25-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Notebook quality](https://github.com/johnnyone89/TCFN4PVForecasting/actions/workflows/notebook-quality.yml/badge.svg)](https://github.com/johnnyone89/TCFN4PVForecasting/actions/workflows/notebook-quality.yml)
[![TCFN DOI](https://img.shields.io/badge/DOI-10.23023%2FJPT.2026.14.1.003-2F80ED)](https://doi.org/10.23023/JPT.2026.14.1.003)

[Overview](#overview) · [Workflow](#reproduction-workflow) · [Run](#quick-start) · [Expected results](#expected-results) · [Citation](#citation)

</div>

---

## Overview

This repository provides the datasets and executable notebooks used for photovoltaic (PV) power forecasting with:

- **TCFN — Trend–Context Fusion Network**, combining 1D-CNN, multi-head attention, and LSTM components.
- **TRACE — Temporal Regime-Aware Chronological Ensemble**, using the most recent 168 observed hours to produce a direct 24-hour forecast.

The notebooks follow the same overall sequence described in the paper: data loading, integrity checks, chronological splitting, feature construction, model training, validation-based selection, final refitting, and held-out evaluation.

In TRACE, **chronological** means that measured predictors are restricted to information available at the forecast origin. It does not refer to causal-effect identification.

## Included materials

| Path | Description |
|---|---|
| [`code/TRACE_Guarded_Dual_Strategy_PV_Forecasting.ipynb`](code/TRACE_Guarded_Dual_Strategy_PV_Forecasting.ipynb) | End-to-end TRACE implementation |
| [`code/main_tcfn_pipeline.ipynb`](code/main_tcfn_pipeline.ipynb) | Main TCFN training and evaluation pipeline |
| [`code/benchmark_comparison.ipynb`](code/benchmark_comparison.ipynb) | Benchmark-model comparison |
| [`code/ablation_study_variants.ipynb`](code/ablation_study_variants.ipynb) | TCFN ablation experiments |
| [`data/Dangjin_Landfill_PV_Dataset.csv`](data/Dangjin_Landfill_PV_Dataset.csv) | Dangjin PV and weather data |
| [`data/Gwangyang_Port_Site2_PV_Dataset.csv`](data/Gwangyang_Port_Site2_PV_Dataset.csv) | Gwangyang PV and weather data |

## Reproduction workflow

```mermaid
flowchart LR
    A["PV and weather data"] --> B["Hourly data audit"]
    B --> C["Train / validation / test split"]
    C --> D["Model training and selection"]
    D --> E["24-step forecast and evaluation"]
```

Running the main TRACE notebook from top to bottom performs the following steps:

1. Loads the Dangjin and Gwangyang datasets and checks their columns and hourly timestamps.
2. Reconstructs the study period from January 2015 through August 2019.
3. Applies the same chronological split used in the paper:
   - training: January 2015–April 2017;
   - validation: May 2017–June 2018;
   - test: July 2018–August 2019.
4. Uses the preceding 168 hours to construct each forecasting origin.
5. Generates forecasts for `t+1` through `t+24`.
6. Selects the feature profile and prediction strategy using validation data.
7. Refits the selected model with the combined training and validation periods.
8. Evaluates the final model on the held-out test period and exports the tables and figures.

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/johnnyone89/TCFN4PVForecasting.git
cd TCFN4PVForecasting
```

### 2. Create the environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The reference TRACE environment used Python 3.9.25, pandas 2.3.3, NumPy 2.0.2, scikit-learn 1.6.1, and PyTorch 2.8.0.

For the TensorFlow-based TCFN notebooks, additionally run:

```bash
pip install -r requirements-tcfn.txt
```

### 3. Check the datasets

The following files must contain the study observations:

```text
data/Dangjin_Landfill_PV_Dataset.csv
data/Gwangyang_Port_Site2_PV_Dataset.csv
```

The required columns and study coverage are listed in [`data/README.md`](data/README.md). You may also point TRACE to another data directory by setting `TRACE_DATA_DIR`.

> **Current data status:** the CSV files presently visible in the public repository are empty filename placeholders. The actual study datasets must be uploaded before an external user can reproduce the reported results.

### 4. Run the notebook

```bash
jupyter lab code/TRACE_Guarded_Dual_Strategy_PV_Forecasting.ipynb
```

Open the notebook and run all cells sequentially. Generated predictions, evaluation tables, figures, and model bundles are saved to `TRACE_outputs/`.

## Expected results

With the same datasets, chronological split, and modeling settings, the reproduced performance should be close to the values reported in the paper:

| Site | Approximate RMSE | Approximate MAE | Approximate R² |
|---|---:|---:|---:|
| Dangjin | about 101 kW | about 51 kW | about 0.83 |
| Gwangyang | about 167 kW | about 83 kW | about 0.82 |

Exact values may differ slightly depending on the operating system, package build, hardware, and numerical backend. The reproduced values should nevertheless remain close to the reported range when the same data, split, random seeds, and execution order are used.

## Notes

- Execute notebook cells in order rather than running isolated later sections.
- Do not use the held-out test period to revise the selected configuration.
- Keep zero-generation periods in the primary evaluation, as implemented in the notebook.
- The main purpose of this repository is methodological reproduction; bit-for-bit numerical identity across every environment is not expected.

## Citation

For the published TCFN study, please cite:

> Shin, Y.; Moon, J. **Trend–Context Fusion Network with Multi-Head Attention for Solar Photovoltaic Power Forecasting.** *Journal of Platform Technology* **2026**, *14*(1), 3–21. https://doi.org/10.23023/JPT.2026.14.1.003

Citation information for TRACE will be added after publication.

## Contact

**Jihoon Moon, Ph.D.**<br>
Assistant Professor, Department of Data Science<br>
Duksung Women's University, Seoul 01369, Republic of Korea<br>
[jmoon25@duksung.ac.kr](mailto:jmoon25@duksung.ac.kr)
