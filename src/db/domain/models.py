from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text
from uuid import UUID

from src.db.domain.database import Base

class User(Base):
    __tablename__: str = "users"

    username: Mapped[str] = mapped_column(default="Rennamed user")
    email: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    projects: Mapped[list["Project"]] = relationship(back_populates="creator")
    tasks: Mapped[list["Task"]] = relationship(back_populates="creator")

class Task(Base):
    __tablename__: str = "tasks"

    name: Mapped[str] = mapped_column(default="nameless task")
    description: Mapped[str] = mapped_column(Text)
    importance_status: Mapped[str]
    color: Mapped[str]
    project_id: Mapped[UUID] = mapped_column(ForeignKey("projects.id"))
    creator_id: Mapped[UUID | None] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    creator: Mapped["User"] = relationship(back_populates="tasks")
    performers_ids: Mapped[list["User"] | None] = relationship(
        User,
        secondary="m2m_users_tasks",
        lazy="selectin"
    )

class Subtask(Base):
    __tablename__: str = "subtasks"

    name: Mapped[str] = mapped_column(default="nameless subtask")
    description: Mapped[str] = mapped_column(Text)
    importance_status: Mapped[str]
    task_id: Mapped[UUID] = mapped_column(ForeignKey("tasks.id", ondelete="SET NULL"), nullable=False)
    creator_id: Mapped[UUID] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    performer_id: Mapped[UUID] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

class Project(Base):
    __tablename__: str = "projects"

    name: Mapped[str] = mapped_column(default="nameless project")
    description: Mapped[str | None] = mapped_column(Text)
    color: Mapped[str]
    performers_ids: Mapped[list[User]] = relationship(
        User,
        secondary="m2m_users_projects",
        lazy="selectin",
    )
    creator_id: Mapped[UUID | None] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    creator: Mapped["User"] = relationship(back_populates="projects")

class UserProject(Base):
    __tablename__: str = "m2m_users_projects"

    project_id: Mapped[UUID] = mapped_column(
        ForeignKey("projects.id", ondelete="CASCADE"), index=True,
    )
    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), index=True,
    )

class UserTask(Base):
    __tablename__: str = "m2m_users_tasks"

    task_id: Mapped[UUID] = mapped_column(
        ForeignKey("tasks.id", ondelete="CASCADE"), index=True,
    )
    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), index=True,
    )