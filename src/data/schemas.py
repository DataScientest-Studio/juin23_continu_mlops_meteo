from datetime import datetime
from pydantic import BaseModel

class WeatherAUS(BaseModel):
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

   class Config:
      orm_mode = True

'''
class User(BaseModel):
   username: str


class User_Create(User):
   password: str

'''



