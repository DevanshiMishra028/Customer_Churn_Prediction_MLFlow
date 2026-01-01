
from model.load_model import loadmodel
import pandas as pd
from fastapi import FastAPI

from pydantic import BaseModel, Field

app = FastAPI(title="Customer Churn Prediction")

model = loadmodel()


class InputData(BaseModel):
    gender: int
    SeniorCitizen: int
    Partner: int
    Dependents: int
    tenure: float
    PhoneService: int
    MultipleLines: int
    OnlineSecurity: int
    OnlineBackup: int
    DeviceProtection: int
    TechSupport: int
    StreamingTV: int
    StreamingMovies: int
    PaperlessBilling: int
    MonthlyCharges: float
    TotalCharges: float
    InternetService_DSL: int
    InternetService_Fiber_optic: int = Field(alias="InternetService_Fiber optic")
    Contract_One_year: int = Field(alias="Contract_One year")
    Contract_Two_year: int = Field(alias="Contract_Two year")
    PaymentMethod_Credit_card_automatic: int = Field(alias="PaymentMethod_Credit card (automatic)")
    PaymentMethod_Electronic_check: int = Field(alias="PaymentMethod_Electronic check")
    PaymentMethod_Mailed_check: int = Field(alias="PaymentMethod_Mailed check")

    class Config:
        allow_population_by_field_name = True



@app.get("/")
def health_check():
    return {"status": "API is running"}


@app.post("/predict")
def predict(data: InputData):
    df = pd.DataFrame([data.dict(by_alias=True)])
    prediction = model.predict(df)
    return {"prediction": int(prediction[0])}
