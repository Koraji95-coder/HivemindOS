from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_daphne_ask():
    payload = {"prompt": "Hello Daphne"}
    response = client.post("/api/daphne/ask", json=payload)
    assert response.status_code == 200
    assert "response" in response.json()
