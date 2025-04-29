from pydantic import BaseModel
from uuid import UUID
from datetime import date

from src.db.projects.enums import Color

class CreateProjectSchema(BaseModel):
    name: str
    description: str | None
    color: Color
    final_date: date
    performers_ids: list[UUID] | UUID | None

    class Config:
        from_attributes = True