# Module 6: Model Logging

## What is Model Logging?
Model Logging stores a trained model in MLflow along with all required files for **reloading, reproducibility, and deployment**.

## What Gets Logged?
- Trained model
- Model configuration
- Dependencies & environment
- Model signature *(optional)*
- Input example *(optional)*
- Metadata

## Important Functions

| Function | Purpose |
|----------|---------|
| `log_model()` | Logs model as an **artifact** inside an MLflow run |
| `save_model()` | Saves model locally without experiment tracking |
| `load_model()` | Loads a saved/logged model for inference |

## `log_model()` vs `save_model()`

| `log_model()` | `save_model()` |
|---------------|----------------|
| Requires MLflow run | No run required |
| Tracked in MLflow UI | Local storage only |
| Best for MLOps | Best for backup/sharing |

> 💡 **Remember:** Use **`log_model()`** for experiment tracking and **`save_model()`** only for local storage.

--- ---

# Module 7: Model Signature

## What is Model Signature?
A **Model Signature** defines the expected **input and output schema** of a model. It acts as the model's **API contract**.

## Signature Contains
- Input features
- Data types
- Output format
- (Optional) Input shape

## Types
- **Input Schema:** Expected feature names and datatypes.
- **Output Schema:** Prediction format returned by the model.

## Creating Signature
- **Automatic:** `infer_signature(X_train, prediction)`
- **Manual:** Define schema explicitly.

## Benefits
- Input validation
- Prevents datatype mismatch
- Better API documentation
- Safer deployment
- Improves reproducibility

> 💡 **Remember:** Signature defines the **structure**, not the actual data.

--- ---

# Module 8: Input Example

## What is `input_example`?
A sample input stored with the model to demonstrate the expected prediction request.

## Purpose
- Documentation
- Request validation
- API testing
- Easier deployment

## Example
```python
input_example = X_train.iloc[:5]
```

## Signature vs Input Example

| Signature | Input Example |
|-----------|---------------|
| Defines schema | Provides sample data |
| Feature names & types | Actual feature values |
| Used for validation | Used for documentation |

> 💡 **Remember:** **Signature = Rules**, **Input Example = Sample**.

--- ---

# Module 9: Model Metadata

## What is Metadata?
Metadata is information **about the model**, helping identify, organize, and reproduce it.

## Common Metadata
- Model name
- Version
- Author
- Framework
- Dataset
- Description
- Training date
- Git commit
- Tags

## Why Metadata?
- Easy search
- Better collaboration
- Version tracking
- Documentation
- Reproducibility

## Metadata vs Tags

| Metadata | Tags |
|----------|------|
| System & user information | User-defined labels |
| Version, framework, date | Author, team, dataset version |

> 💡 **Remember:** **Metadata describes the model**, while **Tags help categorize it**.

--- ---

# Module 10: MLflow Models

## What is an MLflow Model?
An **MLflow Model** is a standardized directory containing the trained model, configuration, dependencies, and environment files for deployment.

## Typical Structure
```
model/
├── MLmodel
├── model.pkl
├── conda.yaml
├── requirements.txt
└── python_env.yaml
```

## Important Files

| File | Purpose |
|------|---------|
| **MLmodel** | Main configuration (Blueprint) |
| **model.pkl** | Serialized trained model |
| **conda.yaml** | Conda environment |
| **requirements.txt** | Python package dependencies |
| **python_env.yaml** | Python runtime details |

## Workflow
```text
Train → log_model() → MLflow Model Directory → load_model() → Deployment
```

> 💡 **Remember:** The **MLmodel** file tells MLflow **how to load and serve the model**.

--- --- 

# ⭐ Quick Revision (Modules 6–10)

| Term | Meaning |
|------|---------|
| **Model Logging** | Saving a model for reproducibility and deployment |
| **Flavor** | Framework-specific format (e.g., sklearn, pytorch, xgboost) |
| **`log_model()`** | Log model as an MLflow artifact |
| **`save_model()`** | Save model locally |
| **`load_model()`** | Load model for inference |
| **Model Signature** | Input/output schema of the model |
| **`input_example`** | Sample input stored with the model |
| **Metadata** | Information describing the model |
| **MLmodel** | Main configuration file (Blueprint) |
| **model.pkl** | Serialized trained model |