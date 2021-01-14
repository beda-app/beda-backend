from typing import Any

from fastapi import APIRouter
from fastapi import Body
from fastapi import HTTPException

from ...database import User
from .models import RegisterResponse
from .utils import create_access_token
from .utils import get_password_hash
from .utils import is_password_secure
from .utils import is_valid_email

__all__ = ("router",)

router = APIRouter()


@router.post("/register", response_model=RegisterResponse)
async def register(email: str = Body(...), password: str = Body(...)) -> Any:
    email = email.lower()
    if await User.filter(email=email).count() != 0:
        raise HTTPException(status_code=400, detail="User already registered!")
    if not is_valid_email(email):
        raise HTTPException(status_code=400, detail="Invalid email!")
    if not is_password_secure(password):
        raise HTTPException(status_code=400, detail="Unsecure password!")

    user = User(email=email, password=get_password_hash(password))
    await user.save()
    return RegisterResponse(token=create_access_token({"user": user.id}))
