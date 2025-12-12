from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse

from todolist_fastapi.classes import Task
from todolist_fastapi.dir import templates

from data.data import tasks

router = APIRouter(tags=["tasks"],
                   responses={404: {"description": "Not found"}}
)


task_id_counter = 0

@router.get("/", response_class=HTMLResponse)
async def read_tasks(request: Request):
    """Главная страница со списком задач"""
    return templates.TemplateResponse("index.html", {
        "request": request,
        "tasks": tasks,
        "task_count": len(tasks),
        "completed_count": len([t for t in tasks if t.completed])
    })

@router.post("/add-task")
async def add_task(title: str = Form(...)):
    """Добавление новой задачи"""
    global task_id_counter
    new_task = Task(id=task_id_counter, title=title)
    tasks.append(new_task)
    task_id_counter += 1
    return RedirectResponse(url="/", status_code=303)

@router.post("/toggle-task/{task_id}")
async def toggle_task(task_id: int):
    """Переключение статуса выполнения задачи"""
    for task in tasks:
        if task.id == task_id:
            task.completed = not task.completed
            break
    return RedirectResponse(url="/", status_code=303)

@router.post("/delete-task/{task_id}")
async def delete_task(task_id: int):
    """Удаление задачи"""
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return RedirectResponse(url="/", status_code=303)

# # API endpoints для будущего использования
# @router.get("/api/tasks")
# async def get_tasks_api():
#     """API для получения списка задач"""
#     return [task.to_dict() for task in tasks]
#
# @router.get("/health")
# async def health_check():
#     """Health check endpoint"""
#     return {"status": "healthy", "framework": "FastAPI", "package_manager": "Poetry"}