#pytest uniwst test example tt

from fastapi.testclient import TestClient 

from src.api.api import app 

secret = d05669a75db8538349e3cfbe3c8d0b13f9b4cddc6725602e74ffe7fb981e31d8 

client = TestClient(app)

def test_main_status():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "API 1.0.1 = OK (by Issam B.)"}
