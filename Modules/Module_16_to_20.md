# Module 16: Model Versioning ⭐

## What is Model Versioning?
**Model Versioning** maintains multiple versions of the same registered model, making it easy to track changes, compare performance, and rollback when needed.

## Why?
- Prevents overwriting old models
- Easy rollback
- Tracks deployment history
- Improves reproducibility

## Versioning Workflow
```text
Train Model
      ↓
log_model()
      ↓
Register Model
      ↓
Version Created (V1, V2...)
      ↓
Assign Alias
      ↓
Deploy
```

## Aliases
Instead of using version numbers, assign meaningful names:
- Champion
- Candidate
- Production
- Shadow
- Canary
- Latest

## Champion-Challenger Strategy
```text
Champion (Current Production)
            ↓
      Train New Model
            ↓
       Challenger Model
            ↓
        Performance Test
            ↓
 Better? ─── Yes ──► New Champion
            │
            No
            ↓
     Keep Current Champion
```

> 💡 **Remember:** **Version = Number**, **Alias = Human-readable name** pointing to that version.

---

# Module 17: Model Serving ⭐

## What is Model Serving?
**Model Serving** makes a trained model available for predictions through a **REST API**.

## Serving Workflow
```text
Client
   ↓
HTTP Request
   ↓
MLflow Server
   ↓
Model Prediction
   ↓
HTTP Response
```

## Serve Locally
```bash
mlflow models serve
```

Default prediction endpoint:
```text
POST /invocations
```

## Types of Inference

| Batch Inference | Online Inference |
|-----------------|------------------|
| Large dataset | Single request |
| Offline | Real-time |
| Scheduled | On-demand |
| Higher latency | Low latency |

## Testing Tools
- Postman
- curl
- Python `requests`

> 💡 **Remember:** **Batch = Many predictions together**, **Online = One prediction at a time**.

---

# Module 18: MLflow Projects ⭐

## What are MLflow Projects?
MLflow Projects provide a **standard project structure** for reproducible ML execution across different environments.

## Standard Structure
```text
project/
├── MLproject
├── main.py
├── conda.yaml
├── requirements.txt
└── data/
```

## Important Files

| File | Purpose |
|------|---------|
| `MLproject` | Project configuration |
| `main.py` | Main execution script |
| `conda.yaml` | Conda environment |
| `requirements.txt` | Python dependencies |

## Execution Workflow
```text
MLproject
     ↓
Create Environment
     ↓
Run Entry Point
     ↓
Training / Evaluation
     ↓
Results
```

## Run Project
```bash
mlflow run .
```

> 💡 **Remember:** Use **`mlflow run`** instead of `python main.py` for reproducible execution.

---

# Module 19: Environment Management ⭐

## What is Environment Management?
Ensures a model runs with the **same software versions** used during training, improving reproducibility.

## Environment Files

| File | Purpose |
|------|---------|
| `requirements.txt` | Pip dependencies |
| `conda.yaml` | Complete Conda environment |
| `python_env.yaml` | Python runtime details |
| `Dockerfile` | Full application environment |

## Workflow
```text
Training Environment
        ↓
Save Dependencies
        ↓
Share Model
        ↓
Recreate Environment
        ↓
Same Results
```

## Virtual Environments
- `venv`
- `virtualenv`
- `Conda`

## Docker
Packages:
- Application
- Model
- Dependencies
- Operating System

> 💡 **Remember:** Same **Code + Dependencies + Versions = Reproducible Results**.

---

# Module 19: Environment Management ⭐

## What is Environment Management?
Ensures a model runs with the **same software versions** used during training, improving reproducibility.

## Environment Files

| File | Purpose |
|------|---------|
| `requirements.txt` | Pip dependencies |
| `conda.yaml` | Complete Conda environment |
| `python_env.yaml` | Python runtime details |
| `Dockerfile` | Full application environment |

## Workflow
```text
Training Environment
        ↓
Save Dependencies
        ↓
Share Model
        ↓
Recreate Environment
        ↓
Same Results
```

## Virtual Environments
- `venv`
- `virtualenv`
- `Conda`

## Docker
Packages:
- Application
- Model
- Dependencies
- Operating System

> 💡 **Remember:** Same **Code + Dependencies + Versions = Reproducible Results**.

---

# Module 20: MLflow CLI ⭐

## What is MLflow CLI?
The **MLflow Command Line Interface (CLI)** provides commands to manage experiments, projects, models, and tracking servers.

## Common Commands

| Command | Purpose |
|---------|---------|
| `mlflow ui` | Launch MLflow UI |
| `mlflow run` | Execute an MLflow Project |
| `mlflow models serve` | Serve model as REST API |
| `mlflow models predict` | Run predictions |
| `mlflow server` | Start Tracking Server |
| `mlflow gc` | Remove deleted runs & artifacts |

## Overall MLflow Workflow
```text
Train Model
      ↓
Track Experiment
      ↓
Log Model
      ↓
Register Model
      ↓
Create Version
      ↓
Assign Alias
      ↓
Serve Model
      ↓
REST API
      ↓
Application
      ↓
Prediction
```

> 💡 **Remember:** The CLI lets you perform most MLflow tasks **without writing Python code**.
---

# ⭐ Quick Revision (Modules 16–20)

| Term | Meaning |
|------|---------|
| **Model Versioning** | Maintain multiple versions of a model |
| **Alias** | Human-readable name for a model version |
| **Champion** | Current production model |
| **Challenger** | New model competing for production |
| **Model Serving** | Expose model via REST API |
| **Batch Inference** | Offline prediction on large datasets |
| **Online Inference** | Real-time prediction |
| **MLflow Projects** | Standardized project packaging |
| **Environment Management** | Recreate the same training environment |
| **MLflow CLI** | Command-line tools for MLflow operations |
---
