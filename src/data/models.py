from sqlalchemy import Boolean, Column, ForeignKey, Integer, Float, String, DateTime, VARCHAR

from data.database import Base

'''
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True) 
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
'''



class WeatherAUS(Base):
    __tablename__ = 'weatheraus_data'

    Date = Column(DateTime, primary_key=True, index=True)
    Location = Column(VARCHAR, index=True)
    MinTemp = Column(VARCHAR, index=True)
    MaxTemp = Column(VARCHAR, index=True)
    Rainfall = Column(VARCHAR, index=True)
    Evaporation = Column(VARCHAR, index=True)
    Sunshine = Column(VARCHAR, index=True)
    WindGustDir = Column(VARCHAR, index=True)
    WindGustSpeed = Column(VARCHAR, index=True)
    WindDir9am = Column(VARCHAR, index=True)
    WindDir3pm = Column(VARCHAR, index=True)
    WindSpeed9am = Column(VARCHAR, index=True)
    WindSpeed3pm = Column(VARCHAR, index=True)
    Humidity9am = Column(VARCHAR, index=True)
    Humidity3pm = Column(VARCHAR, index=True)
    Pressure9am = Column(VARCHAR, index=True)
    Pressure3pm = Column(VARCHAR, index=True)
    Cloud9am = Column(VARCHAR, index=True)
    Cloud3pm = Column(VARCHAR, index=True)
    Temp9am = Column(VARCHAR, index=True)
    Temp3pm = Column(VARCHAR, index=True)
    RainToday = Column(VARCHAR, index=True)
    RainTomorrow  = Column(VARCHAR, index=True)

    '''
    model pour la BDD local
    
        date = Column(DateTime, primary_key=True, index=True)
    location = Column(VARCHAR, index=True)
    mintemp = Column(VARCHAR, index=True)
    maxtemp = Column(VARCHAR, index=True)
    rainfall = Column(VARCHAR, index=True)
    evaporation = Column(VARCHAR, index=True)
    sunshine = Column(VARCHAR, index=True)
    windgustdir = Column(VARCHAR, index=True)
    windgustspeed = Column(VARCHAR, index=True)
    winddir9am = Column(VARCHAR, index=True)
    winddir3pm = Column(VARCHAR, index=True)
    windspeed9am = Column(VARCHAR, index=True)
    windspeed3pm = Column(VARCHAR, index=True)
    humidity9am = Column(VARCHAR, index=True)
    humidity3pm = Column(VARCHAR, index=True)
    pressure9am = Column(VARCHAR, index=True)
    pressure3pm = Column(VARCHAR, index=True)
    cloud9am = Column(VARCHAR, index=True)
    cloud3pm = Column(VARCHAR, index=True)
    temp9am = Column(VARCHAR, index=True)
    temp3pm = Column(VARCHAR, index=True)
    raintoday = Column(VARCHAR, index=True)
    raintomorrow  = Column(VARCHAR, index=True)
        
    '''

