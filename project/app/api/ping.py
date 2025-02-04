from fastapi import APIRouter, Depends

from app.config import Settings, get_settings
import logfire

router = APIRouter()


@router.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    with logfire.span("Get Ping"):
        logfire.info("Pong!")

        return {
            "ping": "pong!",
            "environment": settings.environment,
            "testing": settings.testing,
        }
