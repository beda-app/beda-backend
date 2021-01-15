from pydantic import BaseModel


class RegisterResponse(BaseModel):
    token: str


class LoginResponse(BaseModel):
    token: str
