### Bibliothèque pour OAuth2
import uvicorn
import pandas as pd
import random

from datetime import datetime, timedelta

from fastapi import FastAPI, Body, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# Bibliothèque pour chargement du modèle de prédiction
from fastapi.responses import FileResponse, StreamingResponse
import pickle
import io
import nest_asyncio

# Initialisation de l'API
app = FastAPI(
    title="DST/MLOPS -- PROJET METEO --- API",
    description="API develppée par Issam Benhadda pour le projet Météo en Australie - MLOps (Août 2021)",
    version = "1.0.1")

@app.get('/', tags=["Test de l'API"])
async def read_api():
    return "API 1.0.1 = OK (by Issam B.)" 


@app.get('/welcome', tags=["Test de l'API"])
async def read_welcome():
    return "Bienvenue dans l'API créée par Issam B."


@app.post('/pred', responses=reponses_HTTP, dependencies=[Depends(allow_access)], tags=["Prédiction via pickle"])
def get_prediction(data: data):
    received = data.dict()
    Location = received['Location']
    Rainfall = received['Rainfall']
    WindGustDir = received['WindGustDir']
    WindGustSpeed = received['WindGustSpeed'] 
    WindDir9am = received['WindDir9am']
    WindDir3am = received['WindDir3am']
    WindSpeed9am = received['WindSpeed9am']
    WindSpeed3am = received['WindSpeed3am']
    Humidity9am = received['Humidity9am']
    Humidity3am = received['Humidity3am']
    Pressure3pm = received['Pressure3pm']
    Temp3pm = received['Temp3pm']
    RainToday = received['RainToday']

    prediction = loaded_model.predict_proba([[Location, Rainfall, WindGustDir, WindGustSpeed,
                                        WindDir9am, WindDir3am, WindSpeed9am, WindSpeed3am,
					Humidity9am, Humidity3am, Pressure3pm, Temp3pm, RainToday]])[:, 1]
   

    return prediction[0]



nest_asyncio.apply()

# added by MDG to test pytest

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)


