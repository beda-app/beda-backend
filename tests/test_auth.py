import random
import string

import pytest
from fastapi.testclient import TestClient
from jose import jwt

from app import app
from app.config import settings
from app.routes.auth.utils import ALGORITHM

client = TestClient(app)


def random_string(length: int) -> str:
    return "".join(random.sample(string.digits + string.ascii_lowercase, length))


def generate_random_email():
    return random_string(8) + "@" + random_string(8) + "." + random_string(3)


def generate_random_password():
    return "".join(random.sample(string.digits + string.ascii_letters, 8))


def test_registration():
    password = generate_random_password()
    email = generate_random_email()

    response = client.post(
        "/auth/register", json={"email": email, "password": password}
    )

    assert response.ok
    assert (
        jwt.decode(
            response.json()["token"], settings.SECRET_KEY, algorithms=[ALGORITHM]
        ).get("user")
        == 1
    )

    response = client.post(
        "/auth/register", json={"email": email, "password": password}
    )

    assert not response.ok


def test_login():
    password = generate_random_password()
    email = generate_random_email()

    assert client.post("/auth/register", json={"email": email, "password": password}).ok

    assert client.post("/auth/login", json={"email": email, "password": password}).ok
