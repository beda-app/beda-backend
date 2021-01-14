import asyncio

import pytest

from app.database import close as close_tortoise
from app.database import init as init_tortoise

TORTOISE_ORM_TEST_CONFIG = {
    "connections": {"default": "sqlite://:memory:"},
    "apps": {
        "models": {
            "models": ["app.database.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.mark.asyncio
@pytest.fixture(scope="session", autouse=True)
async def initialize_tests():
    await init_tortoise()
    yield
    await close_tortoise()
