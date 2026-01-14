from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import db_conn
from .associations import images_to_projects


class Image(db_conn.Model):
    def __repr__(self):
        return self.filename

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    filename: Mapped[str] = mapped_column(String, nullable=False)
    projects = relationship(
        "Project",
        secondary=images_to_projects,
        back_populates="images",
    )
