import logging

from fastapi import FastAPI

from app.api import ping, summaries
from app.db import init_db
from contextlib import asynccontextmanager


log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(
        summaries.router, prefix="/summaries", tags=["summaries"]
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
