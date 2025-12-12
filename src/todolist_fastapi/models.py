from pydantic import BaseModel


# Pydantic модели для будущего использования с базой данных
class TaskBase(BaseModel):
    title: str
    completed: bool = False


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True