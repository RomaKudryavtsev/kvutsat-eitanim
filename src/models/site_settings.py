from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from .base import db_conn


class SiteSettings(db_conn.Model):
    def __repr__(self):
        return f"<SiteSettings {self.id}>"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    phone: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    address: Mapped[str] = mapped_column(String, nullable=False)
    hours: Mapped[str] = mapped_column(String, nullable=False)
