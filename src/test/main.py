from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel
import pickle
import uvicorn
import io
import pandas as pd
import nest_asyncio

app = FastAPI()

#Creating a class for the attributes input to the ML model.
class data(BaseModel):
	Location : float 
	Rainfall : float 
	WindGustDir : float
	WindGustSpeed : float
	WindDir9am : float
	WindDir3am : float
	WindSpeed9am : float
	WindSpeed3am : float
	Humidity9am : float
	Humidity3am : float
	Pressure3pm : float
	Temp3pm: float
	RainToday : float


#Loading the trained model
with open("./model.pkl", "rb") as f:
    loaded_model = pickle.load(f)
    
@app.post('/')
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

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

