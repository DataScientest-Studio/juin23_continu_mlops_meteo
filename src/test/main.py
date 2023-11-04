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

#Loading the trained model - Test CICD
#with open("model.pkl", "rb") as f:
#    loaded_model = pickle.load(f)

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

nest_asyncio.apply()

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

