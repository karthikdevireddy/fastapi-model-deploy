# Project Lifecycle and setup

This repository hosts a machine learning model deployed as a RESTful API using FastAPI. It leverages a RandomForestClassifier model trained on NY building data, 
offering an endpoint for making predictions.

## Project tree

.fastapi-model-deploy
 * [train_app](./train_app)
   * retrain.py - training/re-training
 * [infra_app](./infra_app)
   * app.py - Flask API file
   * incomemodel.py - pydantic for input validation
   * Dockerfile - serving container
   * download_latest_model.py - Download latest model from mlflow
   * requirements.txt
 * [data](./data)
   * train - training data
   * test - testing data
 * [notebooks](./notebooks)
   -- Data analysis/preprocessing 
 * [models](./models)
   -- save trained model to this dir
 * README-infra-CICD.md
   * My design for a production grade model
 * README-setup.md
   * Instructions for setting up and running the repo
 
## Prerequisites
* python 3.9+
* pip
* docker

## Instruction 
1. Clone the repo
2. Create a virtual env
3. Install the dependencies for model training in train_app.
   * pip install -r requirements.txt
4. run 'retrain.py' --> 'python retrain.py' 
   * mlflow will be up and running locally and the new model that we currently trained will be register 
   * navigate to the Mlflow url to check out.
   * You will see the model saved in models directory
5. Now move to infra_app directory
   * run 'download_latest_model.py'
   * this will connect to mlflow get the latest model and saves in the pwd.
6. Run Dockerfile to build the image
   * 'docker build -t flask-api .'
   * 'docker run -p 8000:8080 flask-api'
7. Test the api.
   * connect to api docs and test