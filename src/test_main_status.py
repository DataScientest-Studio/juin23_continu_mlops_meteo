#pytest uniwst test example test 2

from fastapi.testclient import TestClient 

# Added by Issam B. for pytest
import sys  
sys.path.append('src')

from src.api.api import app 

client = TestClient(app)

def test_main_status():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "API 1.0.1 = OK (by Issam B.)"}
