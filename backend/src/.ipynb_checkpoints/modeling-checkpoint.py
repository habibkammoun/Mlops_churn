import os
from data_preprocessing_training import transform_data
import pandas as pd
import mlflow
from treatement import xgboost_model
from treatement import random_forest_model

os.environ['MLFLOW_TRACKING_USERNAME']= "__"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "__"

#setup mlflow
mlflow.set_tracking_uri('https://dagshub.com/rami4real/mymlproject.mlflow') #your mlfow tracking uri

#setup mlflow
mlflow.set_experiment("churn-experiment")

#Data Url and version
version = "v2.0"
data_url = "../../data/customer_churn_dataset.csv"

#read the data
df = pd.read_csv(data_url)

#cleaning and preprocessing
X_train,X_test,y_train,y_test = transform_data(df)

#Execute the models with new version of data:
xgboost_model(data_url,version,df,X_train,y_train,X_test,y_test)
random_forest_model(data_url,version,df,X_train,y_train,X_test,y_test)