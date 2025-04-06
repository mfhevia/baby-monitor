from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/alive")
    assert response.status_code == 200
    assert response.json() == {"message": "I am alive baby"}
