from sqlalchemy import Boolean, Column, ForeignKey, Integer, Float, String, DateTime, VARCHAR

from data.database import Base


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


