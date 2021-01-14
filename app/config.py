from pydantic import BaseSettings

__all__ = ("settings",)


class Settings(BaseSettings):
    TORTOISE_URI: str = "sqlite://:memory:"

    # openssl rand -hex 32
    SECRET_KEY: str = "7b3fdcb3cca440480b8eb0f859763bd4a3f2b771eafa09c6e53dfa0dc37149fd"


settings = Settings()
