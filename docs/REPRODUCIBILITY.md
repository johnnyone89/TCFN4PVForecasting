# TRACE reproducibility guide

This guide separates the complete TRACE experiment from the reviewer-revision companion so that each notebook's evidence boundary is explicit.

## 1. Environment

The recorded experiment reported:

| Component | Version |
|---|---:|
| Python | 3.9.25 |
| pandas | 2.3.3 |
| NumPy | 2.0.2 |
| scikit-learn | 1.6.1 |
| PyTorch | 2.8.0 |

Use scikit-learn 1.6.1 when loading the archived joblib bundles. Loading pickled estimators with a different scikit-learn version can produce compatibility warnings or altered behavior.

Install the common environment from the repository root:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 2. Main TRACE pipeline

Notebook: `code/TRACE_Guarded_Dual_Strategy_PV_Forecasting.ipynb`

Required local inputs:

- `data/Dangjin_Landfill_PV_Dataset.csv`
- `data/Gwangyang_Port_Site2_PV_Dataset.csv`

The notebook performs, in order:

1. schema and hourly-continuity audit;
2. fixed chronological partitioning;
3. rolling-origin 168-to-24 sample construction;
4. leakage-safe feature generation;
5. validation-only feature-profile and strategy selection;
6. training-plus-validation refit;
7. one-time held-out test evaluation;
8. controlled persistence and neural-network benchmarks;
9. date-block uncertainty and dependence-aware paired testing;
10. ablations, global XAI, horizon-specific XAI, local SHAP, and saved inference bundles.

The expected target split is January 2015–April 2017 for training, May 2017–June 2018 for validation, and July 2018–August 2019 for testing.

## 3. Reviewer-revision companion

Notebook: `code/TRACE_Reviewer_Revision_AllInOne.ipynb`

Required local artifact:

```text
input/TRACE_PV24_outputs.zip
```

The archive must contain exactly one matching member for each required suffix, including:

- `TRACE_PV24_Guarded_Dual_Strategy_Ensemble_Windows_Jupyter.ipynb`
- both study CSV files;
- `TRACE_PV24_final_results.csv`;
- both `*_all_models_paired_test_predictions.csv` files;
- validation-search tables, saved TRACE bundles, and source figures used by later sections.

An optional local manuscript may be placed at `input/TRACE_submission_manuscript.docx`. The notebook hashes it for provenance when present but does not need it for the numerical analyses.

The companion produces six output groups:

| Directory | Content |
|---|---|
| `outputs/01_scope_benchmark/` | Overall, solar-eligible, actual-positive, and actual-zero comparisons |
| `outputs/02_model_specs/` | Candidate ranges, selected TRACE settings, and neural parameter counts |
| `outputs/03_revised_figures/` | Complete next-day trajectories, horizon-wise RMSE, and source-resolution audit |
| `outputs/04_shap_reexport/` | Readability-adjusted local SHAP waterfalls from unchanged fitted models |
| `outputs/05_weight_sensitivity/` | Validation-selection weight sensitivity |
| `outputs/06_summary/` | Reviewer action matrix, insertion text, integrity table, and output manifest |

## 4. Information-boundary safeguards

- No measured input after forecast origin `t` enters a prediction.
- Target-time calendar and solar-position variables are future-known by construction.
- The weather proxy uses prior-day information rather than measured future weather.
- Feature profiles, thresholds, expert weights, and hurdle/direct-all strategy are fixed from training and validation only.
- Alternative RMSE/MAE weights are post-hoc robustness checks and do not redefine the primary configuration from test performance.
- The test period is evaluated after the decision is locked.

## 5. Lightweight validation

The repository includes a dependency-free notebook syntax check:

```bash
python scripts/check_notebooks.py
```

This parses every notebook and compiles each Python code cell. It does not train models or validate numerical reproduction; those checks require the study data and archived artifacts.

## 6. Generated and sensitive files

Model bundles, checkpoints, local manuscript copies, large prediction archives, and generated outputs are excluded through `.gitignore`. Before publishing any additional artifact, confirm its redistribution rights and remove local paths or credentials.
