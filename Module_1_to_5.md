# Module 1: Introduction to MLflow

## What is MLflow?
- **MLflow** is an open-source MLOps platform for managing the complete Machine Learning lifecycle.
- It helps **track experiments, package models, register versions, and deploy models**.

## Why MLflow?
- Keeps all experiments organized.
- Makes experiments reproducible.
- Enables model versioning.
- Simplifies collaboration.
- Centralizes metrics, parameters, and artifacts.

## ML Lifecycle
```
Data → Preprocessing → Training → Evaluation → Tracking → Registry → Deployment → Monitoring
```

## Core Components
| Component | Purpose |
|-----------|---------|
| **Tracking** | Log experiments (params, metrics, artifacts) |
| **Models** | Standard model packaging |
| **Registry** | Model version management |
| **Serving** | Deploy model as REST API |
| **Projects** | Reproducible ML project structure |

## Key Terms
- **Experiment:** Collection of related runs.
- **Run:** One execution of training code.
- **Metadata:** Information about an experiment (author, metrics, params, etc.).
- **Reproducibility:** Ability to recreate the same results.

> 💡 **Remember:** MLflow manages the **ML lifecycle**, not model training itself.

--- ---

# Module 2: MLflow Tracking

## Tracking
MLflow Tracking records everything generated during a model training run.

## Important Objects
- **Experiment:** Container for multiple runs.
- **Run:** One model training execution.
- **Run ID:** Unique identifier for every run.

## What Can Be Logged?

| Type | Example |
|------|---------|
| **Parameters** | Learning rate, Epochs, Batch size |
| **Metrics** | Accuracy, Loss, Precision |
| **Tags** | Author, Dataset Version, Git Commit |
| **Artifacts** | Model, Images, CSV, Reports |

## Parameter vs Metric
- **Parameter:** Input before training.
- **Metric:** Output during/after training.

## Step
Represents an iteration (Epoch, Batch, Iteration) used for time-series metrics.

## Nested Runs
Used for Grid Search, Optuna, Hyperparameter Tuning, and Cross Validation.

> 💡 **Remember:** Parameters are mostly **constant**, while metrics **change over time**.

--- ---

# Module 3: MLflow UI

## Purpose
The MLflow UI provides a visual interface to manage and compare experiments.

## Main Sections
- Experiments
- Runs
- Parameters
- Metrics
- Artifacts
- Tags

## Features
- Compare multiple runs.
- Visualize metric graphs.
- Search experiments.
- Filter runs by parameters or metrics.
- Download logged artifacts.

## Search Examples
- `metrics.accuracy > 0.90`
- `params.learning_rate = 0.001`
- `tags.author = "Shivansh"`

## Common Uses
- Find the best-performing model.
- Compare hyperparameter tuning results.
- Analyze training history.
- Access saved models and reports.

> 💡 **Remember:** The UI only visualizes data already logged through MLflow Tracking.


--- --- 

# Module 4: Searching Runs

## What is Search?
MLflow allows you to **programmatically search and filter experiment runs** using `mlflow.search_runs()`.

## Purpose
- Retrieve specific runs.
- Compare experiment results.
- Find the best-performing model.
- Automate experiment analysis.

## Search Filters
- **Metrics:** `accuracy > 0.95`
- **Parameters:** `learning_rate = 0.001`
- **Tags:** `author = "Shivansh"`
- **Status:** `FINISHED`, `FAILED`, `RUNNING`
- **Date:** Today, Last Week, Last Month

## SQL-like Filter Example
```python
metrics.accuracy > 0.95
params.learning_rate = "0.001"
tags.author = "Shivansh"
attributes.status = "FINISHED"
```

> 💡 **Remember:** `mlflow.search_runs()` returns a **Pandas DataFrame**, making analysis easy.


--- ---

# Module 5: Autologging

## What is Autologging?
**Autologging** automatically records experiment details without manually calling logging functions.

## Enable
```python
mlflow.autolog()
```

## Automatically Logs
- Parameters
- Metrics
- Model
- Artifacts
- Model Signature
- Input Example (supported libraries)
- Training Information

## Supported Libraries
- Scikit-learn
- TensorFlow / Keras
- PyTorch Lightning
- XGBoost
- LightGBM
- CatBoost
- Spark MLlib

## Advantages
- Less code
- Consistent logging
- Fast experimentation
- Great for beginners

## Limitations
- Less control over logged data.
- Not ideal for custom training loops.

> 💡 **Remember:** Use **Autologging** for quick experiments and **Manual Logging** when you need full control.

--- --- 

#  Quick Revision (Modules 1–5)

| Term | Meaning |
|------|---------|
| **Experiment** | Collection of related runs |
| **Run** | One execution of model training |
| **Parameter** | Input before training (e.g., learning rate) |
| **Metric** | Performance value (e.g., accuracy, loss) |
| **Tag** | Extra metadata (author, dataset version, git commit) |
| **Artifact** | Generated files (model, plots, reports, CSV, etc.) |
| **Step** | Iteration number (epoch, batch, iteration) |
| **Tracking** | Logs experiment details |
| **Registry** | Stores and versions models |
| **Autologging** | Automatically logs supported experiment details |
| **Search Runs** | Filters runs using SQL-like expressions |