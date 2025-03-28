from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_non_existing():
    response = client.get("/not-found")
    assert response.status_code == 404
