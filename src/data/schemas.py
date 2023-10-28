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

   '''
   schema pour la BDD local

   date : datetime = None
   location : str
   mintemp : str
   maxtemp : str
   rainfall : str
   evaporation : str
   sunshine : str
   windgustdir : str
   windgustspeed : str
   winddir9am : str
   winddir3pm : str
   windspeed9am : str
   windspeed3pm : str
   humidity9am : str
   humidity3pm : str
   pressure9am : str
   pressure3pm : str
   cloud9am : str
   cloud3pm : str
   temp9am : str
   temp3pm : str
   raintoday : str
   raintomorrow  : str
   
   '''


   class Config:
      orm_mode = True

'''
class User(BaseModel):
   username: str


class User_Create(User):
   password: str

'''



