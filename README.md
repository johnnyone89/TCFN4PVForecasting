# TCFN and TRACE for Solar Photovoltaic Power Forecasting

This repository provides the official implementation and reproducibility resources for two photovoltaic (PV) power forecasting frameworks:

1. TCFN: Trend–Context Fusion Network with Multi-Head Attention for Solar Photovoltaic Power Forecasting
2. TRACE: Temporal Regime-Aware Causal Ensemble Learning for Rolling 24-Step Photovoltaic Power Forecasting

The repository is intended to support methodological transparency, experimental reproducibility, and further research in data-driven PV power forecasting across geographically and operationally distinct solar-generation environments.

---

## Overview

Accurate PV power forecasting is essential for renewable-energy scheduling, energy-storage management, reserve allocation, and reliable power-system operation. However, PV generation is characterized by strong diurnal patterns, rapid weather-driven changes, site-specific operating conditions, and a substantial concentration of zero-generation observations.

This repository includes two complementary forecasting approaches developed to address these challenges.

### TCFN

TCFN is a hybrid deep-learning architecture that integrates:

- 1D-CNN for local trend extraction
- Multi-Head Attention for broader contextual dependency modeling
- LSTM for sequential feature learning
- SHAP for post-hoc explainability

TCFN was evaluated using PV datasets collected from two distinct Korean environments:

- Dangjin Landfill, representing an inland PV site
- Gwangyang Port Site 2, representing a coastal PV site

The implementation includes the main TCFN training pipeline, benchmark comparisons, ablation experiments, and SHAP-based interpretation.

### TRACE

TRACE is a leakage-resistant and interpretable ensemble-learning framework designed for hourly rolling 24-step PV power forecasting. It maps the most recent 168 hours of observed history directly to forecasts from t + 1 to t + 24 while preserving the operational information boundary at each forecast origin.

TRACE incorporates:

- Training-derived structural-zero identification
- Leakage-safe PV, weather, calendar, and solar-context features
- Chronological selection of feature-memory configurations
- A guarded dual-strategy mechanism
- A hurdle ensemble for activity and positive-magnitude prediction
- A direct-all regression strategy for zero and positive outputs
- Validation-only strategy locking before test evaluation
- Controlled comparisons with persistence and neural-network baselines
- Date-block bootstrap uncertainty estimation
- Dependence-aware statistical testing
- Ablation analysis
- Global, horizon-specific, and local XAI analyses

The complete TRACE experiment is provided in a single executable notebook:

code/TRACE_Guarded_Dual_Strategy_PV_Forecasting.ipynb

This notebook is designed as an end-to-end reproducibility pipeline. Running the notebook sequentially performs data loading, dataset auditing, chronological partitioning, leakage-safe feature engineering, model selection, final refitting, benchmark evaluation, statistical analysis, explainability analysis, and the export of publication-ready tables and figures.

---

## Repository Structure

data/
  Dangjin_Landfill_PV_Dataset.csv
  Gwangyang_Port_Site2_PV_Dataset.csv

code/
  main_tcfn_pipeline.ipynb
      # TCFN training, evaluation, and SHAP-based interpretation

  benchmark_comparison.ipynb
      # Comparison of TCFN with representative baseline models

  ablation_study_variants.ipynb
      # TCFN ablation experiments

  TRACE_Guarded_Dual_Strategy_PV_Forecasting.ipynb
      # Complete end-to-end TRACE pipeline
      # Data auditing, leakage-safe feature construction,
      # chronological validation, guarded strategy selection,
      # direct 24-step forecasting, benchmark evaluation,
      # statistical testing, ablation analysis, XAI,
      # and publication-ready figure and table export

---

## Usage

### 1. Clone the Repository

git clone https://github.com/johnnyone89/TCFN4PVForecasting.git
cd TCFN4PVForecasting

### 2. Install the Required Dependencies

pip install pandas numpy scikit-learn matplotlib shap statsmodels joblib tensorflow torch xgboost catboost jupyter

The exact package versions used in the experiments may also be specified within the corresponding notebooks.

### 3. Prepare the Data

Place the following datasets in the data/ directory:

Dangjin_Landfill_PV_Dataset.csv
Gwangyang_Port_Site2_PV_Dataset.csv

The datasets represent inland and coastal PV-generation environments in the Republic of Korea.

---

## Running the TCFN Experiments

Open and execute the following notebook:

code/main_tcfn_pipeline.ipynb

The notebook performs the core TCFN workflow, including model construction, training, evaluation, and SHAP-based interpretation.

Benchmark and ablation experiments are available in:

code/benchmark_comparison.ipynb
code/ablation_study_variants.ipynb

---

## Running the Complete TRACE Pipeline

Open the following notebook in Jupyter Notebook, JupyterLab, or Google Colab:

code/TRACE_Guarded_Dual_Strategy_PV_Forecasting.ipynb

Execute all notebook cells sequentially from beginning to end.

The notebook performs the complete TRACE workflow in a single integrated environment, including:

1. Dataset loading and integrity checks
2. Hourly timestamp reconstruction
3. Chronological training, validation, and test partitioning
4. Rolling-origin 24-step forecast-window construction
5. Leakage-safe feature engineering
6. Structural-zero identification
7. Full- and short-memory profile evaluation
8. Hurdle and direct-all strategy training
9. Validation-only Pareto-guard selection
10. Final training-plus-validation refitting
11. Direct rolling forecasts from t + 1 to t + 24
12. Persistence and neural-network benchmark comparisons
13. Horizon-wise and trajectory-level evaluation
14. Date-block bootstrap uncertainty estimation
15. Dependence-aware statistical testing
16. Ablation experiments
17. Global and horizon-specific permutation importance
18. TreeSHAP-based local interpretation
19. Export of publication-ready results, figures, and tables

All feature configurations, model-selection decisions, thresholds, and ensemble settings are fixed using the training and validation periods before the held-out test data are evaluated.

---

## Reproducibility Notes

To preserve the integrity of the experiments:

- Data partitions are defined chronologically.
- Feature scaling and model selection are performed without using test-period information.
- Future PV and measured weather observations beyond the forecast origin are excluded.
- Zero-valued PV observations are retained in the primary evaluation.
- Random seeds are predefined rather than selected according to test performance.
- All benchmark models are evaluated under the same direct 24-step forecasting protocol.
- Statistical comparisons account for dependence among overlapping forecast trajectories.

---

## Citation

When using the TCFN implementation, please cite:

Shin, Y.; Moon, J. Trend–Context Fusion Network with Multi-Head Attention for Solar Photovoltaic Power Forecasting. Journal of Platform Technology 2026, 14(1), 3–21.
DOI: 10.23023/JPT.2026.14.1.003

Citation information for TRACE will be added after publication.

---

## Contact

For questions regarding the datasets, implementation, experimental reproduction, or research collaboration, please contact:

Jihoon Moon, Ph.D.
Assistant Professor
Department of Data Science, Duksung Women’s University
Seoul 01369, Republic of Korea
Email: jmoon25@duksung.ac.kr
