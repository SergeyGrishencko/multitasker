from pydantic import BaseModel
from uuid import UUID
from datetime import date

from src.db.projects.enums import Color

class CreateProjectSchema(BaseModel):
    name: str
    description: str | None
    color: Color
    finished_date: date
    # performers_ids: list[UUID] | UUID | None = None

    class Config:
        from_attributes = True

class ResponseProjectSchema(BaseModel):
    name: str
    description: str
    color: Color
    created_date: date
    finished_date: date

class UpdateProjectSchema(BaseModel):
    name: str
    description: str
    color: Color
    finished_date: date
