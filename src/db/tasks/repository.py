from src.db.domain.repository import BaseRepository
from src.db.domain.models import Task

class TaskRepository(BaseRepository):
    model = Task