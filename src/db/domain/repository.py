from sqlalchemy import insert, select

from src.db.domain.database import async_session_maker

class BaseRepository:
    model = None

    @classmethod
    async def create_object(cls, data: dict):
        async with async_session_maker() as session:
            stmt = insert(cls.model).values(**data)
            await session.execute(stmt)
            await session.commit()