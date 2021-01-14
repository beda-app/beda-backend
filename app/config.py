from pydantic import BaseSettings

__all__ = ("settings",)


class Settings(BaseSettings):
    TORTOISE_URI: str = "sqlite://:memory:"


settings = Settings()
