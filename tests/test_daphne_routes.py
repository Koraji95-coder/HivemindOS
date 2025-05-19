"""
test_daphne_routes.py ✅
-------------------------
Unit test for DaphneAgent FastAPI route.
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_daphne_ask():
    """
    Test the /api/daphne/ask endpoint.
    """
    payload = {"prompt": "Hello Daphne"}
    response = client.post("/api/daphne/ask", json=payload)
    assert response.status_code == 200
    assert "response" in response.json()
