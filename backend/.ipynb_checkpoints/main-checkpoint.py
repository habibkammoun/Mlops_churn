from operator import index
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import sklearn
from fastapi import FastAPI, File, UploadFile
import uvicorn
import sys  
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import mlflow
from src.clean_data_csv import clean_data
from src.clean_data_json import clean_data_json
from examplejson.churn_info import ChurnPredictionModel
import json
import os
import mlflow.pyfunc
import pickle
from fastapi import HTTPException
import xgboost

DagsHub_username = os.getenv("DagsHub_username")
DagsHub_token=os.getenv("DagsHub_token")
os.environ['MLFLOW_TRACKING_USERNAME']= "__"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "__"



#setup mlflow
mlflow.set_tracking_uri('https://dagshub.com/rami4real/mymlproject.mlflow/') #your mlfow tracking uri


app = FastAPI()
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#let's call the model from the model registry ( in production stage)

df_mlflow=mlflow.search_runs(filter_string="metrics.F1_score_test < 1")
run_id = df_mlflow.loc[df_mlflow['metrics.F1_score_test'].idxmin()]['run_id']



logged_model = f'runs:/{run_id}/ML_models'

# Load model as a PyFuncModel.
model = mlflow.pyfunc.load_model(logged_model)

@app.get("/")
def read_root():
    return {"Hello": "to churn  detector app version 2"}



@app.post("/predict/csv")
def return_predictions(file: UploadFile = File(...)):
    data = pd.read_csv(file.file)
    preprocessed_data = clean_data(data)
    predictions = model.predict(preprocessed_data)
    return {"predictions": predictions.tolist()}



# this endpoint receives data in the form of json (informations about one transaction)
@app.post("/predict")
def predict(data: ChurnPredictionModel):
    # Convert received data into a DataFrame
    received = data.dict()
    df = pd.DataFrame([received])  # Wrap `received` in a list to create a single-row DataFrame
    # Apply your JSON cleaning function if necessary
    preprocessed_data = clean_data_json(df)

    # Debugging: Check the preprocessed data
    print(preprocessed_data)

    # Predict using the model
    predictions = model.predict(preprocessed_data)

    # Return predictions as JSON
    return {"predictions": predictions.tolist()}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8080)))

