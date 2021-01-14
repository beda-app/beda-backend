from fastapi import FastAPI

from .database import close as close_tortoise
from .database import init as init_tortoise
from .routes import auth_router

app = FastAPI()
app.include_router(auth_router, prefix="/auth")


@app.on_event("startup")
async def startup():
    await init_tortoise()


@app.on_event("shutdown")
async def shutdown():
    await close_tortoise()
