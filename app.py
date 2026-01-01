import pandas as pd
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel , Field 
from typing import Annotated , Optional,Literal
from models.predict import model, MODEL_VERSION



# its good practice that we declare the model version also and generally we take the model version from the "MLflow" which is a special service
app=FastAPI()

# making a pydantic class to validate the data
class price_prediction(BaseModel):
    area : Annotated[int,Field(...,description='this is the areas of the house',example='1200',lt=2000,gt=500)]
    bedrooms : Annotated[int,Field(...,description='this is the no. of bedrooms in the house',example='3',lt=6,gt=1)]
    location : Annotated[Literal['cityA','cityB','cityC'],Field(...,description='this is the location of the house',example='cityA')]
    age : Annotated[int,Field(...,description='this is the age of the house means how old the house is',example=12,lt=30,gt=5)]


@app.get("/")
def home():
    return {"message": "Welcome to the House Price Predictor ...This is the lastest House price predictor traind on the best AI models and the best real world data and hence its relaible and trust worthy"}


@app.post('/predict')
def predict(data:price_prediction):
    input_df=pd.DataFrame([{
        'area':data.area,
        'bedrooms':data.bedrooms,
        'location':data.location,
        'age':data.age
    }])
    prediction=model.predict(input_df)[0]
    return JSONResponse(status_code=200,content={'predicted value is ':prediction}) 



# its often a very good idea to add a health check end point that tells about the current status of our API and it later helps us in telling AWS etc that the API we are going to deploy is not having any issues.

@app.get('/health')
def health_check():
    return {
        'status':'OK',
        'model version':MODEL_VERSION,
        'model loaded': model is not None
    }

