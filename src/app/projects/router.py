from fastapi import APIRouter, HTTPException, status, Depends
from uuid import UUID

from src.app.projects.schemas import CreateProjectSchema, ResponseProjectSchema, UpdateProjectSchema
from src.db.domain.models import User
from src.db.users.dependencies import get_current_user
from src.db.projects.repository import ProjectRepository

router = APIRouter(
    prefix="/project",
    tags=["Projects"]
)

@router.post("/create")
async def create_project(create_data: CreateProjectSchema, user: User = Depends(get_current_user)):
    await ProjectRepository.create_object(create_data.model_dump())

@router.get("/{project_id}")
async def get_project_by_id(project_id: UUID, user: User = Depends(get_current_user)) -> ResponseProjectSchema:
    return await ProjectRepository.get_object(model_id=project_id)

@router.patch("/update/{project_id}")
async def update_project(project_id: UUID, update_data: UpdateProjectSchema, user: User = Depends(get_current_user)) -> ResponseProjectSchema:
    stmt = await ProjectRepository.get_one_or_none(id=project_id)
    if stmt is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    await ProjectRepository.update_object(update_data)
    return await ProjectRepository.get_object(model_id=project_id)

@router.delete("/delete/{project_id}")
async def delete_project(project_id: UUID, user: User = Depends(get_current_user)):
    stmt = await ProjectRepository.get_one_or_none(id=project_id)
    if stmt is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    await ProjectRepository.delete_object(model_id=project_id)
    return stmt