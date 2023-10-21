### Bibliothèque pour OAuth2
import uvicorn
import pandas as pd
import random

from datetime import datetime, timedelta

from fastapi import FastAPI, Body, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from auth.auth_model import User, UserLoginSchema, UserInDB, Token

from auth.auth_handler import users_db, verify_password, get_password_hash, get_user, authenticate_user, create_access_token, get_current_user

from auth.auth_roles import RoleChecker
from auth.auth_roles import get_user, get_current_user


# Bibliothèques pour connection à POSTGRES
from sqlalchemy.orm import Session

from data import crud, models, schemas

from data.schemas import WeatherAUS as SchemaWeatherAUS
from data.models import WeatherAUS as ModelWeatherAUS
from data.database import SessionLocal, engine

from typing import List


# Bibliothèque pour chargement du modèle de prédiction
from fastapi.responses import FileResponse, StreamingResponse
import pickle
import io
import nest_asyncio

from models.predict_model import data


# Initialisation de la BDD POSTGRES
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Initialisation de l'API
app = FastAPI(
    title="DST/MLOPS -- PROJET METEO --- API",
    description="API develppée par Issam Benhadda pour le projet Météo en Australie - MLOps (Août 2021)",
    version = "1.0.1")

reponses_HTTP = {
    200: {"description": "OK : Requête traitée avec succès"},
    404: {"description": "Not Found : Ressource non trouvée"},
    403: {"description": "Forbidden : Authentification OK, droits refusés"},
    401: {"description": "Unauthorized : Authentification nécessaire"},
}

# Initialisation des variables nécessaires à la partie Authorization (Role)
allow_access = RoleChecker(["admin"])
auth_required = RoleChecker(["user", "admin"])


ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Chargement du modèle (via le pickle)
with open("../models/model.pkl", "rb") as f:
    loaded_model = pickle.load(f)


# routes

@app.get('/', tags=["Test de l'API"])
async def read_api():
    return "API 1.0.1 = OK (by Issam B.)" 


@app.get('/welcome', tags=["Test de l'API"])
async def read_welcome():
    return "Bienvenue dans l'API créée par Issam B."


"""@app.get("/myfile", responses=reponses_HTTP, dependencies=[Depends(allow_access)], tags=["Test de l'API"])
def get_myfile():
    return "En attente de chargement du fichier"
"""

@app.get("/myusers", responses=reponses_HTTP, dependencies=[Depends(allow_access)], tags=["Users"])
def get_all_users():
    return users_db


@app.get("/users/connecteduser", tags=["Users"])
async def get_connected_user(current_user: User = Depends(get_current_user)):
    return current_user


@app.post("/token", response_model=Token, tags=["Token Mgt"])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/admin", responses=reponses_HTTP, dependencies=[Depends(allow_access)], tags=["Admin Access"])
async def admin_acess():
    return {
        "data": "Accès Admin"
    }

@app.get("/mydb", responses=reponses_HTTP, dependencies=[Depends(allow_access)], response_model=List[SchemaWeatherAUS], tags=["Lecture de la BDD PostGres"])
async def read_data(db: Session = Depends(get_db)):
    mydb = crud.get_weatherAUS_data(db)
    return mydb

@app.get("/sydneydata", responses=reponses_HTTP, dependencies=[Depends(allow_access)], response_model=List[SchemaWeatherAUS], tags=["Lecture de la BDD PostGres"])
async def read_data(db: Session = Depends(get_db)):
    mysydneydata = crud.get_weatherSYDNEY_data(db)
    return mysydneydata


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