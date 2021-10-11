# project/app/main.py

from fastapi import FastAPI, Depends

from .config import Settings, get_settings

app = FastAPI()

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