# Trend–Context Fusion Network (TCFN) for Solar Photovoltaic Power Forecasting

Official implementation of the paper **“Trend–Context Fusion Network with Multi-Head Attention for Solar Photovoltaic Power Forecasting”** (submitted to the *Journal of Platform Technology*).

## Overview

Accurate forecasting of photovoltaic (PV) power generation is critical for smart-grid stability.  
TCFN is a hybrid deep learning architecture that integrates:

- **1D-CNN** for local trend extraction
- **Multi-Head Attention** for global context modeling
- **LSTM** for sequential dependency learning
- **SHAP** for post-hoc interpretability (XAI)

Experiments on real-world datasets (Dangjin Landfill: inland; Gwangyang Port: coastal) show that TCFN consistently outperforms strong baseline models, including Transformer-based approaches, in terms of RMSE and R².

## Repository Structure

```text
data/
  Dangjin_Landfill_PV_Dataset.csv        # Inland site
  Gwangyang_Port_Site2_PV_Dataset.csv    # Coastal site

code/
  main_tcfn_pipeline.py                  # Grid search + TCFN training + SHAP-based XAI
  benchmark_comparison.py                # Comparison with nine baseline models
  ablation_study_variants.ipynb          # Ablation study experiments
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

### 3) Run benchmark comparisons

```text
python code/benchmark_comparison.py
```

## Citation

If you use this code, please cite the paper (BibTeX will be added after acceptance).

## Contact

For inquiries, please contact the corresponding author.
