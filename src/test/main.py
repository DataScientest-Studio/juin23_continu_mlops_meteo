from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel
import pickle
import uvicorn
import io
import pandas as pd
import nest_asyncio

app = FastAPI()

@app.get("/")
async def read_main():
    return {"msg": "Test CI/CD - API status code"}

nest_asyncio.apply()

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

