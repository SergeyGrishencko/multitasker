from uuid import UUID
from pydantic import BaseModel
from datetime import date

from src.db.domain.enums import Color, ImportanceStatus

class CreateTaskSchema(BaseModel):
    name: str
    description: str
    importance_status: ImportanceStatus
    color: Color
    project_id: UUID
    finished_date: date

class ResponseTaskSchema(BaseModel):
    name: str
    description: str
    created_date: date
    finished_date: date
    importance_status: ImportanceStatus
    color: Color
    project_id: UUID

class UpdateTaskSchema(BaseModel):
    name: str
    description: str
    finished_date: date
    importance_status: ImportanceStatus
    color: Color