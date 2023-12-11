import uvicorn
from fastapi import FastAPI
import pandas as pd
import joblib
from incomemodel import Income
# Initialize the FastAPI app
app = FastAPI()

# Load your trained model
model = joblib.load('mlflow_model.pkl')

@app.post('/v1/predict/')
async def predict(input_data: Income):
    # Convert input data to a pandas DataFrame
    input_dict = input_data.model_dump()
    input_df = pd.DataFrame([input_dict])

    # Get the prediction from the model
    prediction = model.predict(input_df)
    status = 'error' if prediction == -1 else 'success'

    prediction_list = prediction.tolist() if hasattr(prediction, 'tolist') else prediction

    # Return the prediction
    return {
        'statusCode': 200,
        'status': status,
        'probability': prediction_list[0],
    }