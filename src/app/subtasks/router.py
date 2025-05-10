from fastapi import APIRouter, Depends, HTTPException, status
from uuid import UUID

from src.app.subtasks.schemas import CreateSubtaskSchema, ResponseSubtaskSchema, UpdateSubtaskSchema
from src.db.tasks.repository import TaskRepository
from src.db.subtasks.repository import SubtaskRepository
from src.db.users.dependencies import get_current_user
from src.db.domain.models import User

router = APIRouter(
    prefix="/subtask",
    tags=["Subtasks"]
)

@router.post("/create")
async def create_subtask(create_data: CreateSubtaskSchema, user: User = Depends(get_current_user)):
    is_task = await TaskRepository.get_one_or_none(id=CreateSubtaskSchema.task_id)
    if is_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    await SubtaskRepository.create_object(create_data.model_dump())

@router.get("/{subtask_id}")
async def get_subtask_by_id(subtask_id: UUID, user: User = Depends(get_current_user)) -> ResponseSubtaskSchema:
    is_subtask = await SubtaskRepository.get_one_or_none(id=subtask_id)
    if is_subtask is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return is_subtask

@router.patch("/update/{subtask_id}")
async def update_subtask(subtask_id: UUID, update_data: UpdateSubtaskSchema, user: User = Depends(get_current_user)) -> ResponseSubtaskSchema:
    is_subtask = await SubtaskRepository.get_one_or_none(id=subtask_id)
    if is_subtask is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    await SubtaskRepository.update_object(update_data=update_data)
    return await SubtaskRepository.get_object(model_id=subtask_id)

@router.delete("/delete/{subtask_id}")
async def delete_subtask(subtask_id: UUID, user: User = Depends(get_current_user)):
    is_subtask = await SubtaskRepository.get_one_or_none(id=subtask_id)
    if is_subtask is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    await SubtaskRepository.delete_object(model_id=subtask_id)
    return is_subtask