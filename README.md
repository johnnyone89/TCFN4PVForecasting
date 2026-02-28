# Trend–Context Fusion Network (TCFN) for Solar Photovoltaic Power Forecasting

Official implementation of the paper **“Trend–Context Fusion Network with Multi-Head Attention for Solar Photovoltaic Power Forecasting,” published in the *Journal of Platform Technology*.** This repository accompanies our published article and is intended to support transparency, reproducibility, and further research in solar photovoltaic (PV) power forecasting.

---

## Overview

Accurate forecasting of photovoltaic (PV) power generation is critical for smart-grid stability and efficient energy management.  
TCFN is a hybrid deep learning architecture designed to capture both local temporal patterns and broader contextual dependencies by integrating:

- **1D-CNN** for local trend extraction  
- **Multi-Head Attention** for global context modeling  
- **LSTM** for sequential dependency learning  
- **SHAP** for post-hoc interpretability (XAI)

Experiments on real-world datasets from two distinct environments—**Dangjin Landfill** (inland) and **Gwangyang Port** (coastal)—demonstrate that TCFN consistently outperforms strong baseline models, including Transformer-based approaches, in terms of **RMSE** and **R²**.

---

## Repository Structure

```text
data/
  Dangjin_Landfill_PV_Dataset.csv         # Inland site
  Gwangyang_Port_Site2_PV_Dataset.csv     # Coastal site

code/
  main_tcfn_pipeline.ipynb                # Grid search + TCFN training + SHAP-based XAI
  benchmark_comparison.ipynb              # Comparison with nine baseline models
  ablation_study_variants.ipynb           # Ablation study experiments
```

## Usage

### 1) Install dependencies

```text
pip install tensorflow pandas numpy scikit-learn shap matplotlib
```

### 2) Run the main pipeline (TCFN + SHAP)

```text
python code/main_tcfn_pipeline.py
```
> This script performs the core **TCFN training pipeline**, including model training, evaluation, and **SHAP-based interpretability analysis**.

### 3) Run benchmark comparisons

```text
python code/benchmark_comparison.ipynb
```
> This notebook reproduces the comparative experiments against **nine baseline models** reported in the study.

## Citation

If you find this repository useful in your research, please cite:

- Shin, Y.; Moon, J. *Trend–Context Fusion Network with Multi-Head Attention for Solar Photovoltaic Power Forecasting*. *Journal of Platform Technology* **2026**, *14*(1), 3–21. DOI: 10.23023/JPT.2026.14.1.003

## Contact

For inquiries regarding the dataset, implementation, or research collaboration, please contact the corresponding author.
