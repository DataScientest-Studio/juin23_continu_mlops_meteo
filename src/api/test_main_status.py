#pytest unit test example

from fastapi.testclient import TestClient 

from main import app 

client = TestClient(app)

def test_main_status():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
