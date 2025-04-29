from src.db.domain.repository import BaseRepository
from src.db.domain.models import Project

class ProjectRepository(BaseRepository):
    model = Project