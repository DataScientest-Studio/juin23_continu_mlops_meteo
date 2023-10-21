from fastapi.testclient import TestClient 

from main import app 

client = TestClient(app)

data = {
  "NAME_CONTRACT_TYPE": 0,
  "CODE_GENDER": 1,
  "FLAG_OWN_CAR": 0,
  "FLAG_OWN_REALTY": 1,
  "CNT_CHILDREN": 0,
  "AMT_INCOME_TOTAL": 202500,
  "AMT_CREDIT": 406597,
  "AMT_ANNUITY": 24700,
  "EXT_SOURCE_2": 0.262949,
  "EXT_SOURCE_3": 0.139376,
  "AGE": 26,
  "ANCIENNITE": 2
}

def test_main_positive():
    response = client.post("/", json=data)
    assert response.json() == 0.75