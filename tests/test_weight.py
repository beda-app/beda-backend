import random

import pytest
from fastapi.testclient import TestClient

from .utils import generate_random_email
from .utils import generate_random_password
from app import app


@pytest.fixture(scope="function")
def client():
    return TestClient(app)


@pytest.fixture(scope="function")
def token(client):
    password = generate_random_password()
    email = generate_random_email()

    response = client.post(
        "/auth/register", json={"email": email, "password": password}
    )
    return response.json()["token"]


def test_add(token: str, client: TestClient):
    response = client.post(
        "/weight/add", json={"weight": random.randint(1, 100), "token": token}
    )
    assert response.ok
    assert response.json() == "ok"


def test_get(token: str, client: TestClient):
    response = client.post("/weight/get", json={"token": token})
    assert response.ok
    assert response.json() == []

    weight = random.randint(1, 100)
    response = client.post("/weight/add", json={"weight": weight, "token": token})
    assert response.ok

    response = client.post("/weight/get", json={"token": token})
    assert response.ok
    assert len(response.json()) == 1
