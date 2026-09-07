# TabularScout 🔭

[English](README.md) | [简体中文](README_zh.md)

A lightweight and explainable baseline evaluation tool for tabular regression datasets.

TabularScout takes a CSV dataset and a target column, performs a quick data profile, evaluates several representative regression baselines with 5-fold cross-validation, and generates a clean Markdown report.

## Features

- **Data Profiling**  
  Quickly checks the number of samples, features, numeric features, and missing values.

- **Multi-Model Baselines**  
  Evaluates four representative regression baselines:
  - Dummy Regressor
  - Linear Regression
  - Ridge Regression
  - Random Forest Regressor

- **Robust Evaluation**  
  Uses 5-fold cross-validation with Root Mean Squared Error (RMSE).

- **Automated Reporting**  
  Automatically ranks models and generates a Markdown report.

- **Command-Line Interface**  
  Run the complete workflow directly from the terminal.

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
2. Run TabularScout
python -m tabular_scout.cli \
  --data examples/diabetes.csv \
  --target target \
  --output outputs/report.md

Example output:

--- TabularScout Finished ---

Dataset: examples/diabetes.csv
Samples: 442
Features: 10

Best baseline: Linear Regression
Report saved to: outputs/report.md
Example Baseline Results

Results on the scikit-learn Diabetes dataset:

Model	5-Fold CV RMSE	Notes
Linear Regression	54.69	🏆 Best Baseline
Random Forest	58.11	Nonlinear ensemble
Ridge	58.45	L2-regularized linear model
Dummy Baseline	77.26	Mean-value predictor

Lower RMSE indicates better predictive performance.

In this example, the simple Linear Regression baseline outperformed the more complex Random Forest model, illustrating that increased model complexity does not necessarily lead to better generalization.

Why These Baselines?

TabularScout intentionally keeps the model set small.

Each model answers a different question about the dataset:

Dummy Regressor

Does not use the input features and simply predicts the mean target value.

It provides a naive lower baseline:

Are the real models actually learning anything useful from the features?

Linear Regression

Provides a simple linear baseline.

It tests whether the target can already be predicted reasonably well using a weighted linear combination of the input features.

Ridge Regression

Extends Linear Regression with L2 regularization.

It tests whether shrinking large model coefficients can improve generalization and provide a more stable linear baseline.

Random Forest

Provides a nonlinear baseline based on an ensemble of decision trees.

It helps determine whether more complex nonlinear relationships and feature interactions may be worth exploring.

The goal of TabularScout is not exhaustive AutoML. Instead, it provides a fast and interpretable first look at a regression dataset.

Evaluation Strategy

TabularScout uses 5-fold cross-validation.

The dataset is divided into five folds. Each fold is used once as the validation set while the remaining four folds are used for training.

Fold 1: Validation | Train | Train | Train | Train
Fold 2: Train | Validation | Train | Train | Train
Fold 3: Train | Train | Validation | Train | Train
Fold 4: Train | Train | Train | Validation | Train
Fold 5: Train | Train | Train | Train | Validation

The final score is the average RMSE across the five validation runs.

Compared with a single train/test split, cross-validation provides a more robust estimate of generalization performance.

Architecture
tabular-scout/
├── tabular_scout/
│   ├── __init__.py
│   ├── data.py        # Data loading and feature-target split
│   ├── models.py      # Baseline models and 5-fold CV evaluation
│   ├── profile.py     # Dataset profiling
│   ├── report.py      # Markdown report generation
│   └── cli.py         # Command-line interface
│
├── examples/
│   └── diabetes.csv
│
├── outputs/
│   └── report.md
│
├── requirements.txt
├── README.md
├── README_zh.md
└── .gitignore
Pipeline
CSV Dataset
     │
     ▼
Data Profiling
     │
     ▼
Feature / Target Split
     │
     ▼
5-Fold Cross-Validation
     │
     ├── Dummy Regressor
     ├── Linear Regression
     ├── Ridge Regression
     └── Random Forest
     │
     ▼
RMSE Ranking
     │
     ▼
Markdown Report
Current Limitations

The current version intentionally keeps a small and explicit scope:

Regression tasks only
Numeric target only
Numeric features only
No automatic missing-value imputation
No categorical feature encoding
Fixed set of baseline models
No automatic hyperparameter tuning

These limitations are intentional for the first version of the project.

What I Learned

Building TabularScout helped me understand:

why a naive baseline is important before evaluating real models;
how Linear Regression differs from Ridge Regression;
how L2 regularization can reduce sensitivity to unstable coefficients;
why Random Forest can model nonlinear relationships and feature interactions;
why a more complex model does not necessarily perform better;
why a single train/test split can be misleading;
how 5-fold cross-validation provides a more robust evaluation;
how scikit-learn's unified estimator interface makes different models easy to compare;
how to turn a machine-learning experiment into a reusable command-line tool.
Tech Stack
Python
pandas
scikit-learn
argparse
Markdown
Roadmap

Possible future improvements:

Missing-value preprocessing
Categorical feature encoding
Classification support
Configurable cross-validation
Additional evaluation metrics

The current v0.1 intentionally focuses on keeping the workflow small, fast, and understandable.

License

This project is intended for learning and experimentation.