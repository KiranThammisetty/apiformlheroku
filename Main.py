# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 18:54:29 2026

@author: kiran
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json



app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

class model_input(BaseModel):
    Pregnancies :int
    Glucose : int
    BloodPressure: int
    SkinThickness : int
    Insulin: int
    BMI: float
    DiabetesPesigreeFunction: float
    Age:int
    
# loading the saved model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

@app.post('/diabetes_prediction')
def diabetes_pres(input_parameter: model_input):
    
    input_data = input_parameter.json()
    input_dictionary = json.loads(input_data)
    
    preg = input_dictionary['Pregnancies']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPesigreeFunction']
    age = input_dictionary['Age']
    
    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]
    
    prediction = diabetes_model.predict([input_list])
    
    if prediction[0] == 0:
        return 'The person is not Diabetic'
    else:
        return 'The person is Daibetic'