from fastapi import APIRouter, HTTPException, status, Depends
from uuid import UUID

from src.app.tasks.schemas import CreateTaskSchema, ResponseTaskSchema, UpdateTaskSchema
from src.db.tasks.repository import TaskRepository
from src.db.projects.repository import ProjectRepository
from src.db.users.dependencies import get_current_user
from src.db.domain.models import User

router = APIRouter(
    prefix="/task",
    tags=["Tasks"]
)

@router.post("/create")
async def create_task(create_data: CreateTaskSchema, user: User = Depends(get_current_user)):
    is_project = await ProjectRepository.get_one_or_none(id=create_data.project_id)
    if is_project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    await TaskRepository.create_object(create_data.model_dump())

@router.get("/{task_id}")
async def get_task_by_id(task_id: UUID, user: User = Depends(get_current_user)) -> ResponseTaskSchema:
    is_task = await TaskRepository.get_one_or_none(id=task_id)
    if is_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return is_task

@router.patch("/update/{task_id}")
async def update_task(task_id: UUID, update_data: UpdateTaskSchema, user: User = Depends(get_current_user)) -> ResponseTaskSchema:
    is_task = await TaskRepository.get_one_or_none(id=task_id)
    if is_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    await TaskRepository.update_object(update_data=update_data)
    return await TaskRepository.get_object(model_id=task_id)

@router.delete("/delete/{task_id}")
async def delete_task(task_id: UUID, user: User = Depends(get_current_user)):
    is_task = await TaskRepository.get_one_or_none(id=task_id)
    if is_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    await TaskRepository.delete_object(model_id=task_id)
    return is_task