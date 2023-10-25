from fastapi.testclient import TestClient 

from main import app 

client = TestClient(app)

data = {
  "NAME_CONTRACT_TYPE": 0,
  "CODE_GENDER": 1,
  "FLAG_OWN_CAR": 0,
  "FLAG_OWN_REALTY": 1,
  "CNT_CHILDREN": 1,
  "AMT_INCOME_TOTAL": 202500,
  "AMT_CREDIT": 715500,
  "AMT_ANNUITY": 21051,
  "EXT_SOURCE_2": 0.13,
  "EXT_SOURCE_3": 0.13,
  "AGE": 32,
  "ANCIENNITE": 4
}

def test_main():
    response = client.post("/", json=data)
    assert response.status_code == 200
