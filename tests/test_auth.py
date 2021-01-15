import random
import string

from fastapi.testclient import TestClient
from jose import jwt

from .utils import generate_random_email
from .utils import generate_random_password
from app import app
from app.config import settings
from app.routes.auth.utils import ALGORITHM

client = TestClient(app)


def test_registration():
    password = generate_random_password()
    email = generate_random_email()

    response = client.post(
        "/auth/register", json={"email": email, "password": password}
    )

    assert response.ok
    assert (
        jwt.decode(
            response.json()["token"], settings.JWT_SECRET_KEY, algorithms=[ALGORITHM]
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
