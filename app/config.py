from typing import List

from pydantic import BaseSettings

__all__ = ("settings",)


class Settings(BaseSettings):
    TORTOISE_URI: str = "sqlite://:memory:"
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost"]

    # openssl rand -hex 32
    JWT_SECRET_KEY: str = (
        "7b3fd0b3cca440480b8eb0f859763bd4a3f2b771e4fa09c6e53dfa0dc37149fd"
    )


settings = Settings()
