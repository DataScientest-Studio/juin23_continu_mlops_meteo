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
	NAME_CONTRACT_TYPE : float 
	CODE_GENDER : float
	FLAG_OWN_CAR : float
	FLAG_OWN_REALTY : float
	CNT_CHILDREN : float
	AMT_INCOME_TOTAL : float
	AMT_CREDIT : float
	AMT_ANNUITY : float
	EXT_SOURCE_2 : float
	EXT_SOURCE_3 : float
	AGE: float
	ANCIENNITE : float

#Loading the trained model
#with open("model.pkl", "rb") as f:
#    loaded_model = pickle.load(f)
    
@app.post('/')
def get_prediction(data: data):
    received = data.dict()
    NAME_CONTRACT_TYPE = received['NAME_CONTRACT_TYPE']
    CODE_GENDER = received['CODE_GENDER']
    FLAG_OWN_CAR = received['FLAG_OWN_CAR'] 
    FLAG_OWN_REALTY = received['FLAG_OWN_REALTY']
    CNT_CHILDREN = received['CNT_CHILDREN']
    AMT_INCOME_TOTAL = received['AMT_INCOME_TOTAL']
    AMT_CREDIT = received['AMT_CREDIT']
    AMT_ANNUITY = received['AMT_ANNUITY']
    EXT_SOURCE_2 = received['EXT_SOURCE_2']
    EXT_SOURCE_3 = received['EXT_SOURCE_3']
    AGE = received['AGE']
    ANCIENNITE = received['ANCIENNITE']

#    prediction = loaded_model.predict_proba([[NAME_CONTRACT_TYPE, CODE_GENDER, FLAG_OWN_CAR, FLAG_OWN_REALTY,
#                                        CNT_CHILDREN, AMT_INCOME_TOTAL, AMT_CREDIT, AMT_ANNUITY,
#					EXT_SOURCE_2, EXT_SOURCE_3, AGE, ANCIENNITE]])[:, 1]
    
#    return prediction[0]

@app.get("/OK")
def get_image_ok():
    return FileResponse("local0.png")

@app.get("/KO")
def get_image_ko():
    return FileResponse("local1.png")

nest_asyncio.apply()

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

