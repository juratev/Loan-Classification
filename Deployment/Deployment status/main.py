import pickle
import uvicorn
import xgboost
import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()
model = pickle.load(open('1xgb.sav', 'rb'))

class InputData(BaseModel):
  Amount_Requested: int = Field(alias='Amount Requested')
  Loan_Title: str = Field(alias='Loan Title')
  Risk_Score: int = Field(alias='Risk Score')
  Debt_To_Income_Ratio: int = Field(alias='Debt-To-Income Ratio')
  State: str
  Employment_Length: int = Field(alias='Employment Length')
  Application_Year: int = Field(alias='Application Year')
  Application_Month: int = Field(alias='Application Month')

@app.get('/')
def index():
  return {'message': 'It works.'}

@app.post('/predict')
def predict(input_data: InputData):
  X = pd.DataFrame(input_data.dict(by_alias=True), index=[0])
  y_pred = model.predict(X)[0]
  prediction = 'Loan application rejected' if y_pred == 0 else 'Loan application accepted'
  return {'prediction': prediction}


if __name__ == '__main__':
  uvicorn.run(app, host='0.0.0.0', port=8000)

# python -m uvicorn main:app --reload