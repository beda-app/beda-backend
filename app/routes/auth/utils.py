import re
import time
from datetime import datetime
from datetime import timedelta
from typing import Optional

from fastapi import Body
from fastapi import HTTPException
from jose import jwt
from jose import JWTError
from passlib.context import CryptContext  # type: ignore

from ...config import settings
from ...database import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"
EMAIL_REGEX = re.compile(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")


def is_password_secure(password: str) -> bool:
    return len(password) >= 8


def is_valid_email(email: str) -> bool:
    return EMAIL_REGEX.fullmatch(email) is not None


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=1)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Body(None)) -> User:
    invalid_token = HTTPException(status_code=401, detail="Invalid access token!")
    if token is None:
        raise invalid_token
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            options={"require_exp": True},
            algorithms=[ALGORITHM],
        )
    except JWTError:
        raise invalid_token

    user_id: int = payload.get("user")
    if user_id is None:
        raise invalid_token

    user = await User.filter(id=user_id).first()
    if user is None:
        raise invalid_token
    return user
