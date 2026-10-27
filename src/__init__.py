"""
Uttarakhand Flash-Flood Prediction - Objective 2 Core Package
"""

# Keep src.<module> imports stable while source files are grouped by workstream.
from pathlib import Path as _Path

for _workstream in (
    'Data Engineering, Data Quality & Statistical Analysis',
    'Feature Engineering & Predictive Feature Analysis',
    'Predictive Modelling, Hyperparameter Optimisation & Evaluation',
    'Probabilistic Prediction, Uncertainty Quantification & Hybrid Risk Modelling',
):
    __path__.append(str(_Path(__file__).resolve().parent / _workstream))

del _Path, _workstream
