# project/app/main.py
import os

from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise

from .config import Settings, get_settings

app = FastAPI()

register_tortoise(
    app,
    db_url=os.environ.get("DATABASE_URL"),
    modules={"models": ["app.models.tortoise"]},
    generate_schemas=False,
    add_exception_handlers=True,
)

@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    """

    :param settings: the Depends function is a dependency that declares another dependency, get_settings
                    Depends depends on the result of get_settings. The value returned, Settings, is then
                    assigned to the settings parameter
    :return:
    """
    return {
        "ping" : "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }
