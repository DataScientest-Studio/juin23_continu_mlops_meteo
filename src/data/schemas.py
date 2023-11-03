from datetime import datetime
from pydantic import BaseModel

class WeatherAUS(BaseModel):
   Date : datetime = None
   Location : str
   MinTemp : str
   MaxTemp : str
   Rainfall : str
   Evaporation : str
   Sunshine : str
   WindGustDir : str
   WindGustSpeed : str
   WindDir9am : str
   WindDir3pm : str
   WindSpeed9am : str
   WindSpeed3pm : str
   Humidity9am : str
   Humidity3pm : str
   Pressure9am : str
   Pressure3pm : str
   Cloud9am : str
   Cloud3pm : str
   Temp9am : str
   Temp3pm : str
   RainToday : str
   RainTomorrow  : str

   class Config:
      orm_mode = True




