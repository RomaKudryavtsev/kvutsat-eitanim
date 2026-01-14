from datetime import datetime, timezone, timedelta
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .associations import images_to_projects
from .base import db_conn


class Project(db_conn.Model):
    def __repr__(self):
        return self.name

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(tz=timezone(timedelta(hours=3))),
        nullable=False,
    )
    images = relationship(
        "Image",
        secondary=images_to_projects,
        back_populates="projects",
        lazy="joined",
    )
