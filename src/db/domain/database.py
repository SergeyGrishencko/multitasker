from uuid import UUID
from datetime import date, datetime, timezone
from sqlalchemy import Date
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column

from src.db.domain.config import settings

engine = create_async_engine(settings.DATABASE_URL)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(primary_key=True)
    created_date: Mapped[date] = mapped_column(Date, default=datetime.now(timezone.utc))
    finished_date: Mapped[date] = mapped_column(Date, nullable=True, default=datetime.now(timezone.utc))