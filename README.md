<div align="center">

# TRACE & TCFN for Photovoltaic Power Forecasting

**Official reproducibility package for chronological ensemble forecasting and trend–context fusion photovoltaic power prediction**

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![TRACE DOI](https://img.shields.io/badge/TRACE%20DOI-10.3390%2Feng7100515-2F80ED)](https://doi.org/10.3390/eng7100515)
[![TCFN DOI](https://img.shields.io/badge/TCFN%20DOI-10.23023%2FJPT.2026.14.1.003-2F80ED)](https://doi.org/10.23023/JPT.2026.14.1.003)

[Overview](#overview) · [Workflow](#reproduction-workflow) · [Run](#quick-start) · [Citation](#citation)

</div>

---

## Overview

This repository provides the datasets and executable notebooks supporting the published photovoltaic (PV) power forecasting study.

The repository contains two complementary forecasting frameworks:

- **TCFN — Trend–Context Fusion Network**: a deep forecasting architecture integrating convolutional feature extraction, multi-head attention, and LSTM-based temporal representation learning.
- **TRACE — Temporal Regime-Aware Chronological Ensemble**: a chronological forecasting framework designed for direct 24-hour-ahead PV power prediction using the recent 168-hour observation window.

The workflow follows the experimental protocol described in the publication, including data integrity checking, chronological splitting, feature construction, model training, validation-based configuration selection, final refitting, and held-out evaluation.

## Publication

This repository accompanies **two published photovoltaic power forecasting studies**, corresponding to the TRACE and TCFN implementations provided here.

### TRACE

> **Moon, J. TRACE: Temporal Regime-Aware Chronological Ensemble Learning for Rolling 24-Step Photovoltaic Power Forecasting.** *Eng* **2026**, *7*(10), 515.  
> DOI: https://doi.org/10.3390/eng7100515  
> Article: https://www.mdpi.com/2673-4117/7/10/515

The TRACE study presents a **Temporal Regime-Aware Chronological Ensemble Learning** framework for rolling direct 24-step photovoltaic power forecasting under a chronological information boundary.

### TCFN

> **Shin, Y.; Moon, J. Trend–Context Fusion Network with Multi-Head Attention for Solar Photovoltaic Power Forecasting.** *Journal of Platform Technology* **2026**, *14*(1), 3–21.  
> DOI: https://doi.org/10.23023/JPT.2026.14.1.003  
> Journal issue: https://jpt.ictps.org/all_volumes/volume11volume14/volume-14-no-1

The TCFN study introduces the **Trend–Context Fusion Network**, integrating convolutional feature extraction, multi-head attention, and LSTM-based temporal representation learning for photovoltaic power forecasting.

Accordingly, this repository serves as the reproducibility companion for **both TRACE and TCFN**.

## Included materials

| Path | Description |
|---|---|
| `code/TRACE_Guarded_Dual_Strategy_PV_Forecasting.ipynb` | End-to-end TRACE implementation |
| `code/main_tcfn_pipeline.ipynb` | Main TCFN training and evaluation pipeline |
| `code/benchmark_comparison.ipynb` | Benchmark comparison experiments |
| `code/ablation_study_variants.ipynb` | TCFN ablation experiments |
| `data/` | PV generation and meteorological datasets |

## Reproduction workflow

The notebooks reproduce the complete experimental pipeline:

1. Loads PV generation and meteorological datasets.
2. Performs data integrity checks and timestamp validation.
3. Applies the chronological train/validation/test protocol.
4. Constructs historical input windows.
5. Generates multi-step PV power forecasts.
6. Selects configurations using validation performance only.
7. Refits the selected model configuration.
8. Evaluates performance on the held-out test period.
9. Exports prediction results, tables, and figures.

For TRACE, chronological forecasting means that predictors are restricted to information available at the forecast origin. It does not imply causal-effect identification.

## Quick start

```bash
git clone https://github.com/johnnyone89/TCFN4PVForecasting.git
cd TCFN4PVForecasting

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\\Scripts\\activate

python -m pip install --upgrade pip
pip install -r requirements.txt
```

For the TensorFlow-based TCFN implementation:

```bash
pip install -r requirements-tcfn.txt
```

Run the notebooks sequentially:

```bash
jupyter lab code/TRACE_Guarded_Dual_Strategy_PV_Forecasting.ipynb
```

## Experimental protocol

The study uses a strict chronological evaluation setting:

- Training period: January 2015–April 2017
- Validation period: May 2017–June 2018
- Test period: July 2018–August 2019

The forecasting task uses the preceding 168 hours to generate direct forecasts from `t+1` to `t+24`.

The held-out test period is not used for hyperparameter selection, configuration revision, or model design decisions.

## Reproducibility notes

Small numerical differences may occur depending on:

- operating system;
- Python package versions;
- GPU/CUDA configuration;
- deep-learning backend implementation; and
- floating-point computation.

The repository is intended for scientific reproduction of the reported experimental workflow rather than forcing identical numerical outputs across every environment.

## Citation

If you use this repository, its code, datasets, forecasting workflows, or experimental protocols in academic work, please cite the publication corresponding to the material you use.

### TRACE

Use this citation for the TRACE notebook, chronological ensemble framework, rolling 24-step forecasting protocol, or TRACE-related results:

> Moon, J. **TRACE: Temporal Regime-Aware Chronological Ensemble Learning for Rolling 24-Step Photovoltaic Power Forecasting.** *Eng* **2026**, *7*(10), 515. https://doi.org/10.3390/eng7100515

```bibtex
@article{moon2026trace,
  author  = {Moon, Jihoon},
  title   = {TRACE: Temporal Regime-Aware Chronological Ensemble Learning for Rolling 24-Step Photovoltaic Power Forecasting},
  journal = {Eng},
  year    = {2026},
  volume  = {7},
  number  = {10},
  pages   = {515},
  doi     = {10.3390/eng7100515},
  url     = {https://doi.org/10.3390/eng7100515}
}
```

### TCFN

Use this citation for the TCFN architecture, TCFN notebooks, or TCFN-related results:

> Shin, Y.; Moon, J. **Trend–Context Fusion Network with Multi-Head Attention for Solar Photovoltaic Power Forecasting.** *Journal of Platform Technology* **2026**, *14*(1), 3–21. https://doi.org/10.23023/JPT.2026.14.1.003

```bibtex
@article{shin2026tcfn,
  author  = {Shin, Y. and Moon, J.},
  title   = {Trend--Context Fusion Network with Multi-Head Attention for Solar Photovoltaic Power Forecasting},
  journal = {Journal of Platform Technology},
  year    = {2026},
  volume  = {14},
  number  = {1},
  pages   = {3--21},
  doi     = {10.23023/JPT.2026.14.1.003},
  url     = {https://doi.org/10.23023/JPT.2026.14.1.003}
}
```

If your work uses **both TRACE and TCFN components**, please cite **both publications**.

## Contact

**Jihoon Moon, Ph.D.**  
Assistant Professor, Department of Data Science  
Duksung Women's University, Seoul 01369, Republic of Korea  
[jmoon25@duksung.ac.kr](mailto:jmoon25@duksung.ac.kr)
