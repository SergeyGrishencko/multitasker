from src.db.domain.repository import BaseRepository
from src.db.domain.models import Subtask

class SubtaskRepository(BaseRepository):
    model = Subtask