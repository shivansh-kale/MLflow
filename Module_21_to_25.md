# Module 21: Backend Store ⭐

## What is Backend Store?
The **Backend Store** is the **database** that stores **experiment metadata** (not actual model files).

## Stores
- Experiments
- Runs
- Parameters
- Metrics
- Tags
- Run Status
- Timestamps
- Run IDs

> ❌ **Does NOT store:** Models, Images, CSVs, PDFs, Checkpoints.

## Supported Databases

| Database | Best For |
|----------|----------|
| SQLite | Learning & Local |
| MySQL | Medium-scale Projects |
| PostgreSQL | Production (Most Common) |

## Workflow
```text
Training
     ↓
log_param()
log_metric()
set_tag()
     ↓
Backend Store
(Database)
```

> 💡 **Remember:** **Backend Store = Metadata Database**, **NOT File Storage**.
---

# Module 22: Artifact Store ⭐

## What is Artifact Store?
The **Artifact Store** stores all **files** generated during an ML experiment.

## Stores
- Models
- Images
- CSV Files
- JSON
- Reports
- Checkpoints
- TensorBoard Logs

## Storage Options
- Local Storage
- Amazon S3 ⭐
- Azure Blob Storage
- Google Cloud Storage (GCS)
- MinIO
- NFS

## Artifact Structure
```text
Experiment
      ↓
    Run
      ↓
 ├── model/
 ├── plots/
 ├── report.pdf
 └── predictions.csv
```

## Backend Store vs Artifact Store

| Backend Store | Artifact Store |
|---------------|----------------|
| Metadata | Files |
| Parameters | Models |
| Metrics | Images |
| Tags | CSV / PDF |

> 💡 **Remember:** **Backend = Database**, **Artifact = File Storage**.

---

# Module 23: Tracking Server ⭐

## What is Tracking Server?
The **Tracking Server** is the central server that receives MLflow logging requests and stores them in the **Backend Store** and **Artifact Store**.

## Architecture
```text
MLflow Client
      │
      ▼
Tracking Server
   ├────────► Backend Store
   │
   └────────► Artifact Store
```

## Local Tracking
```text
Training
    ↓
mlruns/
(Local Folder)
```

✔ Best for:
- Learning
- Personal Projects

## Remote Tracking
```text
Developer A
Developer B
Developer C
      ↓
Tracking Server
      ↓
Backend + Artifact Store
```

✔ Best for:
- Teams
- Cloud
- Production

> 💡 **Remember:** The **Tracking Server** acts as a bridge between MLflow clients and storage.

---

# Module 24: Remote Tracking ⭐

## What is Remote Tracking?
**Remote Tracking** sends experiment logs to a **remote MLflow Tracking Server** instead of storing them locally.

## Set Tracking URI
```python
mlflow.set_tracking_uri()
```

Example:
```text
http://localhost:5000
http://mlflow.company.com
```

## Workflow
```text
Training Code
      ↓
set_tracking_uri()
      ↓
Tracking Server
      ↓
Backend Store + Artifact Store
```

## Local vs Remote

| Local | Remote |
|--------|--------|
| Single User | Multiple Users |
| Local Folder | Central Server |
| No Network | Network Required |
| Learning | Production |

## Authentication
- Username & Password
- API Token
- OAuth

> 💡 **Remember:** `set_tracking_uri()` tells MLflow **where to send experiment logs**.

---

# Module 25: Deployment Architecture ⭐

## Complete MLflow Pipeline
```text
Collect Data
      ↓
Preprocess Data
      ↓
Train Model
      ↓
Track Experiment
      ↓
Register Model
      ↓
Serve Model
      ↓
Application
      ↓
Predictions
      ↓
Monitoring
      ↓
Retrain (if needed)
```

## Pipeline Components

| Step | Purpose |
|------|---------|
| Training | Train & Evaluate Model |
| Tracking | Log Parameters, Metrics & Artifacts |
| Registry | Store & Version Models |
| Serving | Expose REST API |
| Monitoring | Track Production Performance |

## MLflow Responsibilities

| Component | Responsibility |
|-----------|----------------|
| Backend Store | Metadata |
| Artifact Store | Files |
| Tracking Server | Logging |
| Model Registry | Versioning |
| Serving | Inference |
| Monitoring | Model Health |

> 💡 **Remember:** The complete ML lifecycle is **Train → Track → Register → Serve → Monitor → Retrain**.

---

# ⭐ Quick Revision (Modules 21–25)

| Term | Meaning |
|------|---------|
| **Backend Store** | Stores experiment metadata |
| **Artifact Store** | Stores files (models, images, reports) |
| **Tracking Server** | Receives and manages MLflow logs |
| **Remote Tracking** | Logs experiments to a central server |
| **SQLite** | Default local backend database |
| **PostgreSQL** | Recommended production backend |
| **Amazon S3** | Popular artifact storage |
| **Tracking URI** | Address of the MLflow server |
| **Deployment Pipeline** | Train → Track → Register → Serve → Monitor |

---
