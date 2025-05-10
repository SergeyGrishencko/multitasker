from uuid import UUID
from pydantic import BaseModel
from datetime import date

from src.db.domain.enums import ImportanceStatus

class CreateSubtaskSchema(BaseModel):
    name: str
    description: str
    importance_status: ImportanceStatus
    task_id: UUID
    # performer_id: UUID

class ResponseSubtaskSchema(BaseModel):
    name: str
    description: str 
    importance_status: ImportanceStatus

class UpdateSubtaskSchema(BaseModel):
    name: str
    description: str
    finished_date: date
    importance_status: ImportanceStatus