import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import mlflow
import warnings

def random_forest_model(data_url, version, df, x_train, y_train, x_test, y_test):
    mlflow.sklearn.autolog(disable=True)
    with mlflow.start_run(run_name='Random Forest'):
        mlflow.log_param("data_url", data_url)
        mlflow.log_param("data_version", version)
        mlflow.log_param("input_rows", df.shape[0])
        mlflow.log_param("input_cols", df.shape[1])
        rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
        params = rf.get_params()
        mlflow.set_tag(key="model", value="Random Forest")
        mlflow.log_params(params)
        rf.fit(x_train, y_train)
        train_features_name = f'{x_train=}'.split('=')[0]
        train_label_name = f'{y_train=}'.split('=')[0]
        mlflow.set_tag(key="train_features_name", value=train_features_name)
        mlflow.set_tag(key="train_label_name", value=train_label_name)
        predicted = rf.predict(x_test)
        precision, recall, fscore, support = score(y_test, predicted, average='macro')
        mlflow.log_metric("Precision_test", precision)
        mlflow.log_metric("Recall_test", recall)
        mlflow.log_metric("F1_score_test", fscore)
        mlflow.sklearn.log_model(rf, artifact_path="ML_models")

def xgboost_model(data_url, version, df, x_train, y_train, x_test, y_test):
    mlflow.sklearn.autolog(disable=True)
    with mlflow.start_run(run_name='XGBoost'):
        mlflow.log_param("data_url", data_url)
        mlflow.log_param("data_version", version)
        mlflow.log_param("input_rows", df.shape[0])
        mlflow.log_param("input_cols", df.shape[1])
        xgb = XGBClassifier(n_estimators=100, max_depth=10, learning_rate=0.1, random_state=42)
        params = xgb.get_params()
        mlflow.set_tag(key="model", value="XGBoost")
        mlflow.log_params(params)
        xgb.fit(x_train, y_train)
        train_features_name = f'{x_train=}'.split('=')[0]
        train_label_name = f'{y_train=}'.split('=')[0]
        mlflow.set_tag(key="train_features_name", value=train_features_name)
        mlflow.set_tag(key="train_label_name", value=train_label_name)
        predicted = xgb.predict(x_test)
        precision, recall, fscore, support = score(y_test, predicted, average='macro')
        mlflow.log_metric("Precision_test", precision)
        mlflow.log_metric("Recall_test", recall)
        mlflow.log_metric("F1_score_test", fscore)
        mlflow.sklearn.log_model(xgb, artifact_path="ML_models")
