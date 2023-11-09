#pytest

from fastapi.testclient import TestClient 

from src.test.main import app 

client = TestClient(app)

def test_main_status():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Test CI/CD - API status code"}
