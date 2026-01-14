from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from .base import db_conn


class SiteSettings(db_conn.Model):
    def __repr__(self):
        return f"<SiteSettings {self.id}>"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    phone: Mapped[str | None] = mapped_column(String, nullable=True)
    email: Mapped[str | None] = mapped_column(String, nullable=True)
