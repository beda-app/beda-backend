from tortoise import Tortoise

from ..config import settings
from .models import User

__all__ = ("init", "close", "TORTOISE_ORM", "User")

TORTOISE_ORM = {
    "connections": {"default": settings.TORTOISE_URI},
    "apps": {
        "models": {
            "models": ["app.database.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


async def init():
    await Tortoise.init(TORTOISE_ORM)
    await Tortoise.generate_schemas(safe=True)


async def close():
    await Tortoise.close_connections()
