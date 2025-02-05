import logging
import os

from fastapi import FastAPI

from app.api import ping, summaries
from app.db import init_db
from contextlib import asynccontextmanager

import logfire
from tortoise.contrib.fastapi import register_tortoise


logfire.configure()

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(
        summaries.router, prefix="/summaries", tags=["summaries"]
    )
    register_tortoise(
        application,
        db_url=os.getenv("DATABASE_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )

    return application


app = create_application()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start up
    log.info("Starting up...")
    init_db(app)

    yield
    # Shut down
    log.info("Shutting down...")
