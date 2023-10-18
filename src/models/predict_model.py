from pydantic import BaseModel

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