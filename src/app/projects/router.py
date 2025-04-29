from fastapi import APIRouter

from src.app.projects.schemas import CreateProjectSchema
from src.db.projects.repository import ProjectRepository

router = APIRouter(
    prefix="/project",
    tags=["Projects"]
)

@router.post("/create")
async def create_project(create_data: CreateProjectSchema):
    await ProjectRepository.create_object(create_data.model_dump())