import mlflow
from mlflow.sklearn import load_model
import os
import dagshub

mlflow.set_tracking_uri("https://dagshub.com/mdevanshi80/Customer_Churn_Prediction_MLFlow.mlflow")

#os.environ['MLFLOW_TRACKING_USERNAME']= 'mdevanshi80'
#os.environ['MLFLOW_TRACKING_PASSWORD']= '*****************'
#os.environ['MLFLOW_TRACKING_URI']= 'https://dagshub.com/mdevanshi80/Customer_Churn_Prediction_MLFlow.mlflow'


def loadmodel():
    model_uri = f"models:/Random Forest@champion"
    return load_model(model_uri)

