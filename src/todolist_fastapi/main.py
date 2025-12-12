import uvicorn
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

import os

from .config.config import settings
from .api import route

# Создаем приложение
app = FastAPI(
    title="To-Do List with Poetry",
    version="1.0.0",
    description="FastAPI To-Do List application managed with Poetry"
)


app.include_router(route.router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.server_host,
        port=settings.run.server_port,
        reload = True
    )