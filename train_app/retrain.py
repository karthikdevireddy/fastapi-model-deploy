# Import models
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score, f1_score, recall_score, roc_auc_score
import mlflow
import pickle

# Create feature columns
data = pd.read_csv("../data/train_final.csv", index_col="index", low_memory=False)

# display data
print(data.head(1))
print("Data load complete")

# Model name and stage level
model_name = "NY Office building"
model_stage = "Production"


#Here we will need to initiate MLflow to start logging

mlflow.set_tracking_uri("mlruns")
mlflow.set_experiment(f"/ml/{model_name}")


mlflow.start_run()

# Feature Engineering
feature_cols = ["officearea", "comarea", "yearbuilt"]

# split into train and test datasets (before preprocessing to avoid data leakage)
test_size = 0.2

# process training and test data
X = data[feature_cols].copy(deep=True)
y = data["target__office"].copy(deep=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

# run model selection (For now using print but logging can be added)
print("Running model training")

model = RandomForestClassifier(max_depth=2, random_state=0)
model.fit(X_train, y_train)
print("Model Training complete")
y_pred = model.predict(X_test)

# Log mlflow results
mlflow.log_metric("accuracy", accuracy_score(y_test, y_pred))
mlflow.log_metric("f1", f1_score(y_test, y_pred))
mlflow.log_metric("recall", recall_score(y_test, y_pred))
mlflow.log_metric("auc", roc_auc_score(y_test, y_pred))

# log model
log = mlflow.sklearn.log_model(model, artifact_path="sklearn_model", registered_model_name=model_name)
mlflow.end_run()


""" Next steps::->

Add the model to Model registry
Load the old model from model registry 
Compare AUC of new model and staging model
"""

print("Calculating model performance")
# If old_model do not exist > Fail with return False

old_model = None
if old_model is None:
    print("No old model to compare against")

# Calculate performance of new model
new_model_score = cross_val_score(model, X_test, y_test, cv=5, scoring="roc_auc")
print(f"New model roc_auc: {new_model_score.mean()}")

# Return model details
print("Registered the latest model to MLFlow")
