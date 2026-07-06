# Module 11: MLmodel File ⭐

## What is MLmodel?
The **MLmodel** file is the **blueprint** of every MLflow model. It tells MLflow **how to load, interpret, and serve** the model.

## Contains
- Model Flavors
- Model Signature
- Loader Module
- Environment Details
- Metadata
- Creation Time

## Important Fields

| Field | Purpose |
|-------|---------|
| `flavors` | Supported model frameworks |
| `signature` | Input & Output schema |
| `loader_module` | Framework loader |
| `python_function` | Universal PyFunc interface |
| `utc_time_created` | Model creation timestamp |

## Workflow
```text
Train Model
      ↓
log_model()
      ↓
MLmodel File Created
      ↓
MLflow Reads MLmodel
      ↓
Load / Deploy Model
```

> 💡 **Remember:** Without the **MLmodel** file, MLflow doesn't know **how to use the saved model**.
---

# Module 12: Model Flavors

## What is a Flavor?
A **Flavor** defines **how MLflow saves and loads a model** for a specific ML framework.

## Types

| Flavor | Description |
|---------|-------------|
| Native Flavor | Framework-specific (e.g., sklearn, pytorch) |
| PyFunc Flavor | Universal MLflow interface |

## Native vs PyFunc

| Native | PyFunc |
|---------|---------|
| Framework-specific | Framework-independent |
| Uses native APIs | Uses generic API |
| More framework features | Same interface for all models |

## Workflow
```text
Random Forest
      ↓
Save Model
      ↓
MLmodel
   ├── sklearn
   └── python_function
```

> 💡 **Remember:** One model can have **multiple flavors**.

---

# Module 13: PyFunc ⭐

## What is PyFunc?
**PyFunc (Python Function)** is MLflow's **universal model interface**, allowing every supported model to be loaded and predicted using the same API.

## Why Use PyFunc?
- Framework independent
- Standard prediction API
- Easy deployment
- Production friendly

## Generic Prediction
```python
model = mlflow.pyfunc.load_model(path)
model.predict(data)
```

## Workflow
```text
Any ML Framework
       ↓
    PyFunc
       ↓
 predict(data)
```

## Custom PyFunc
Can include:
- Preprocessing
- Feature Engineering
- Business Rules
- Postprocessing

> 💡 **Remember:** PyFunc hides framework differences by exposing a common `predict()` interface.

---

# Module 14: Custom Python Models

## What is a Custom Python Model?
A **PythonModel** allows you to package **custom Python logic**, not just a trained ML model.

## Base Class
```python
class MyModel(PythonModel):
```

## Important Methods

| Method | Purpose |
|---------|---------|
| `load_context()` | Loads resources once during initialization |
| `predict()` | Runs prediction for every request |

## Workflow
```text
Load Model
     ↓
load_context()
     ↓
Resources Loaded
     ↓
predict()
     ↓
Prediction
```

## Use Cases
- NLP pipelines
- Image preprocessing
- Ensemble models
- Recommendation systems
- RAG pipelines

> 💡 **Remember:** `load_context()` runs **once**, while `predict()` runs **every inference request**.

---

# Module 15: Model Registry ⭐

## What is Model Registry?
A **centralized repository** to **store, version, and manage** ML models. Think of it as **GitHub for ML models**.

## Benefits
- Model Versioning
- Central Storage
- Collaboration
- Easy Deployment
- Rollback Support

## Registry Workflow
```text
Train Model
      ↓
log_model()
      ↓
Register Model
      ↓
Version Created
      ↓
Assign Alias (Champion/Candidate)
      ↓
Deploy
```

## Legacy Stages
```text
None
 ↓
Staging
 ↓
Production
 ↓
Archived
```

> ⭐ **Modern MLflow:** Uses **Aliases** (`Champion`, `Candidate`, `Shadow`, `Canary`) instead of fixed stages.

## Experiment vs Registry

| Experiment | Registry |
|------------|----------|
| Stores runs | Stores approved models |
| Used during training | Used after model selection |
| Tracks metrics | Manages versions |

> 💡 **Remember:** **Experiment = Development**, **Registry = Production**.

---

**MLmodel file** = The blueprint of an MLflow model; defines flavors, signature, loader, and environment.
**Flavor** = Framework-specific way to save/load a model (e.g., sklearn, pytorch).
**PyFunc** (python_function) = Universal MLflow interface that exposes every model through the same predict() API.
**Native Flavor** = Uses the original framework's APIs and features.
**Custom PythonModel** = Lets you package arbitrary Python logic, not just a trained ML model.
**load_context()** = Executes once when the model is loaded; use it to load external resources.
**predict()** = Executes on every inference request; contains prediction logic.
**Model Registry** = Central repository for versioning, managing, and deploying models.
**Legacy Stages** = None → Staging → Production → Archived.
**Modern MLflow**= Uses Aliases (e.g., Champion, Candidate) instead of fixed stages for more flexible deployment workflows.

---