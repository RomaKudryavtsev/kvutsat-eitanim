from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# IMPORTANT: SQLAlchemy.session is a session that is scoped to the current Flask application context. It is cleaned up after every request.
# See official documentation: https://flask-sqlalchemy.readthedocs.io/en/stable/quickstart/#check-the-sqlalchemy-documentation
db_conn = SQLAlchemy(model_class=Base)
