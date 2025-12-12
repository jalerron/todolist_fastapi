#Путь для шаблонов
import os

from starlette.templating import Jinja2Templates

current_dir = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(current_dir, "templates")
templates = Jinja2Templates(directory=templates_dir)