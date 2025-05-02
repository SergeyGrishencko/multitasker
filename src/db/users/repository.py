from sqlalchemy import insert
from pydantic import EmailStr

from src.db.domain.repository import BaseRepository
from src.db.domain.database import async_session_maker
from src.db.domain.models import User

class UserRepository(BaseRepository):
    model = User

    @classmethod
    async def create_object(cls, **data):
        async with async_session_maker() as session:
            stmt = insert(cls.model).values(**data)
            await session.execute(stmt)
            await session.commit()