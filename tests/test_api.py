from fastapi.testclient import TestClient
from api_pedidos.api import app
from http import HTTPStatus
import pytest

@pytest.fixture
def client():
    return TestClient(app)

def test_return_200(client):
    response = client.get("/healthcheck")
    assert response.status_code == HTTPStatus.OK

def test_return_json(client):
    response = client.get("/healthcheck")
    assert response.headers["Content-Type"] == "application/json"

def test_return_info(client):
    response = client.get("/healthcheck")
    assert response.json() == {
        "status": "ok"
    }