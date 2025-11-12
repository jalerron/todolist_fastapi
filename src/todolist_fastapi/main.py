import uvicorn
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

import os

from todolist_fastapi.config.config import settings

# Создаем приложение
app = FastAPI(
    title="To-Do List with Poetry",
    version="1.0.0",
    description="FastAPI To-Do List application managed with Poetry"
)

#Путь для шаблонов
current_dir = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(current_dir, "templates")
templates = Jinja2Templates(directory=templates_dir)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.server_host,
        port=settings.run.server_port,
        reload = True
    )