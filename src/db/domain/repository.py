from sqlalchemy import insert, select, update, delete
from uuid import UUID

from src.db.domain.database import async_session_maker

class BaseRepository:
    model = None

    @classmethod
    async def create_object(cls, data: dict):
        async with async_session_maker() as session:
            stmt = insert(cls.model).values(**data)
            await session.execute(stmt)
            await session.commit()
    
    @classmethod
    async def get_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()
        
    @classmethod
    async def get_object(cls, model_id: UUID):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
    
    @classmethod
    async def update_object(cls, update_data: dict):
        async with async_session_maker() as session:
            stmt = update(cls.model).values(**update_data.dict())
            await session.execute(stmt)
            await session.commit()
        
    @classmethod
    async def delete_object(cls, model_id: UUID):
        async with async_session_maker() as session:
            stmt = delete(cls.model).filter_by(id=model_id)
            await session.execute(stmt)
            await session.commit()