from sqlalchemy import Table, Column, Integer, ForeignKey
from ..base import db_conn

images_to_projects = Table(
    "images_to_projects",
    db_conn.metadata,
    Column("image_id", Integer, ForeignKey("image.id"), primary_key=True),
    Column("project_id", Integer, ForeignKey("project.id"), primary_key=True),
)
