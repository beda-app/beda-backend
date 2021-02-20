from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .database import close as close_tortoise
from .database import init as init_tortoise
from .routes import auth_router
from .routes import weight_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth")
app.include_router(weight_router, prefix="/weight")


@app.on_event("startup")
async def startup():
    await init_tortoise()


@app.on_event("shutdown")
async def shutdown():
    await close_tortoise()
