# Module 26: Integration with DVC ⭐

## Why Integrate DVC with MLflow?
**DVC** manages **data**, while **MLflow** manages **experiments and models**. Together they provide complete reproducibility.

## Responsibilities

| DVC | MLflow |
|-----|---------|
| Dataset Versioning | Experiment Tracking |
| Data Pipelines | Model Tracking |
| Large File Storage | Metrics & Parameters |
| Data Reproducibility | Model Registry & Serving |

## Workflow
```text
Dataset
    ↓
Version with DVC
    ↓
Train Model
    ↓
MLflow Logs
(Parameters • Metrics • Artifacts)
```

## Best Practice
Always log the **DVC commit hash** or **dataset version** as an MLflow tag.

```text
dataset_version = v5
dvc_commit = a38df7
```

> 💡 **Remember:** **Git → Code**, **DVC → Data**, **MLflow → Experiments**.
---

# Module 27: Integration with Git ⭐

## Why Git + MLflow?
Git versions your **code**, while MLflow tracks the experiments executed using that code.

## Git Stores
- Source Code
- Commit History
- Branches
- Repository

## Complete Reproducibility
```text
Git Commit
      +
DVC Dataset Version
      +
MLflow Run
      ↓
Reproduce Exact Experiment
```

## Best Practice
Log Git details as MLflow tags:
- `git_commit`
- `git_branch`
- `git_repo`

> 💡 **Remember:** If you can't identify the **code version**, you can't reproduce the experiment.

---

# Module 28: Hyperparameter Tuning ⭐

## What is Hyperparameter Tuning?
Running multiple experiments with different hyperparameter values to find the **best-performing model**.

## Common Methods

| Method | Description |
|--------|-------------|
| Grid Search | Tests every combination |
| Random Search | Random combinations |
| Optuna ⭐ | Intelligent optimization using Bayesian search |

## Nested Runs
```text
Parent Run
      │
      ├── Trial 1
      ├── Trial 2
      ├── Trial 3
      └── Trial 4
```

- **Parent Run:** Complete tuning session
- **Child Run:** One hyperparameter trial

## Best Practices
- One parent run per tuning session
- One child run per trial
- Log all parameters & metrics
- Save only the best model

> 💡 **Remember:** **Nested Runs** keep hyperparameter tuning organized.

---

# Module 29: Deep Learning Logging ⭐

## What Should Be Logged?
- TensorBoard Logs
- Model Checkpoints
- Best Model
- Final Model
- Large Artifacts (Images, Embeddings, ONNX)

## Best Model vs Final Model

| Best Model | Final Model |
|------------|-------------|
| Highest validation performance | Last training epoch |
| Used for deployment | Used for analysis |

## Workflow
```text
Training
    ↓
Save Checkpoints
    ↓
Evaluate Validation
    ↓
Select Best Model
    ↓
Log to MLflow
```

> 💡 **Remember:** The **Best Model** is usually deployed, **not** the Final Model.

---

# Module 30: Production Best Practices ⭐

## Best Practices
- Use meaningful experiment names.
- Keep one experiment per project.
- Organize artifacts into folders.
- Use Registry versions instead of filenames.
- Tag every experiment.
- Clean unused runs regularly.

## Recommended Structure
```text
project/
├── data/
├── src/
├── notebooks/
├── artifacts/
├── MLproject
├── dvc.yaml
└── requirements.txt
```

## Useful Tags
- author
- dataset_version
- git_commit
- framework
- environment
- team

## Cleanup
```bash
mlflow gc
```
Removes permanently deleted runs and artifacts.

> 💡 **Remember:** Good organization makes projects easier to maintain and collaborate on.

---

# Module 31: Common Interview Questions ⭐

## Frequently Asked Comparisons

| Concept | Difference |
|---------|------------|
| Parameter vs Metric | Input vs Output |
| Experiment vs Run | Container vs One Execution |
| Backend vs Artifact Store | Metadata vs Files |
| Registry vs Experiment | Production vs Development |
| `save_model()` vs `log_model()` | Local vs MLflow Tracking |

## Important Questions
- Why use Model Signature?
- Why use PyFunc?
- Why Nested Runs?
- What happens after `set_tracking_uri()`?
- Why separate Backend & Artifact Store?

> 💡 **Remember:** Most MLflow interviews focus on **comparisons** rather than API syntax.

---

# Module 32: End-to-End MLflow Workflow ⭐

## Complete Production Pipeline
```text
Git (Code)
      ↓
DVC (Dataset)
      ↓
Training
      ↓
MLflow Tracking
      ↓
Model Logging
      ↓
Model Registry
      ↓
Model Serving
      ↓
REST API
      ↓
Application
      ↓
Monitoring
      ↓
Retraining
```

## Responsibilities

| Component | Responsibility |
|-----------|----------------|
| Git | Code Versioning |
| DVC | Dataset Versioning |
| MLflow Tracking | Log Experiments |
| Registry | Version Models |
| Serving | Deploy Model |
| Monitoring | Track Production Performance |

> 💡 **Remember:** A production ML pipeline combines **Git + DVC + MLflow**, each solving a different problem.
---

# Module 33: MLflow Internal Working ⭐

## What Happens Inside MLflow?

### Logging Parameters
```text
log_param()
      ↓
MLflow Client
      ↓
Tracking Server
      ↓
Backend Store
```

### Logging Artifacts
```text
log_artifact()
      ↓
Tracking Server
      ↓
Artifact Store
```

### Logging a Model
```text
Trained Model
      ↓
Serialize Model
      ↓
Create MLmodel
Create Environment Files
      ↓
Upload to Artifact Store
      ↓
Update Backend Store
```

## Internal Architecture
```text
Training Script
      ↓
MLflow Client
      ↓
Tracking Server
   ├────────► Backend Store
   └────────► Artifact Store
                ↓
          Model Registry
                ↓
             Serving
                ↓
          Prediction API
```

> 💡 **Remember:** The **Tracking Server** coordinates everything—it routes **metadata** to the Backend Store and **files** to the Artifact Store.

---

# ⭐ Ultimate MLflow Revision

| Component | Responsibility |
|-----------|----------------|
| Git | Version Code |
| DVC | Version Dataset |
| Tracking | Log Experiments |
| Backend Store | Store Metadata |
| Artifact Store | Store Files |
| Tracking Server | Handle Logging Requests |
| Model Logging | Save Deployable Models |
| Model Registry | Version Models |
| Aliases | Point to Production Versions |
| Serving | Expose REST API |
| Monitoring | Track Production Models |
| PyFunc | Universal Prediction API |
| MLmodel | Model Blueprint |
| Projects | Reproducible Execution |
| CLI | Manage MLflow via Terminal |

### 🚀 Complete MLflow Lifecycle
```text
Code (Git)
      ↓
Dataset (DVC)
      ↓
Train
      ↓
Track
      ↓
Register
      ↓
Version + Alias
      ↓
Serve
      ↓
Monitor
      ↓
Retrain
```