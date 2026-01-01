import pandas as pd
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel , Field 
from typing import Annotated , Optional,Literal
import pickle

#loading the model
with open('models/lr_model.pkl','rb') as f:
    model=pickle.load(f)

app=FastAPI()

# making a pydantic class to validate the data
class price_prediction(BaseModel):
    area : Annotated[int,Field(...,description='this is the areas of the house',example='1200',lt=2000,gt=500)]
    bedrooms : Annotated[int,Field(...,description='this is the no. of bedrooms in the house',example='3',lt=6,gt=1)]
    location : Annotated[Literal['cityA','cityB','cityC'],Field(...,description='this is the location of the house',example='cityA')]
    age : Annotated[int,Field(...,description='this is the age of the house means how old the house is',example=12,lt=30,gt=5)]

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


