from sqlalchemy import Boolean, Column, ForeignKey, Integer, Float, String, DateTime, VARCHAR

from src.data.database import Base

'''
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True) 
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
'''



class WeatherAUS(Base):
    __tablename__ = 'weatheraus_data'

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

