import flask_login
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from .base import db_conn


class User(db_conn.Model, flask_login.UserMixin):
    def __repr__(self):
        return f"<User {self.username}>"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        """Returns the user ID as a string for Flask-Login compatibility."""
        return str(self.id)
