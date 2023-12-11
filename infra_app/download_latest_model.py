import os
import sys
import joblib
import mlflow
from mlflow.tracking import MlflowClient

# Configuration
model_name = "NY Office building"
model_stage = "Production"

# Create MlflowClient object

mlflow.set_tracking_uri("../train_app/mlruns")

client = MlflowClient()
model_version = client.get_latest_versions(name=model_name, stages=["None"])
model_version_obj = model_version[0]
version_number = model_version_obj.version
run_id = model_version_obj.run_id

model_uri = f"runs:/{run_id}/sklearn_model"
try:
    # Save current version of model
    model = mlflow.sklearn.load_model(model_uri)
    if model is None:
        raise Exception(f"No {model_stage} model found for {model_name}")
    joblib.dump(model, "../infra_app/mlflow_model.pkl", compress=3)
except Exception as e:
    raise Exception(f"Error while saving model: {e}")