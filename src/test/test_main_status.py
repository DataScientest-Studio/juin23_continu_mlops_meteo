#pytest 1

from fastapi.testclient import TestClient 

from main import app 

client = TestClient(app)

def test_main_status():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "API 1.0.1 = OK (by Issam B.)"}
