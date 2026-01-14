from sqlalchemy import select
from ..models import db_conn, Project


class ProjectRepo:
    def get_all_projects(self) -> list[Project]:
        statement = select(Project)
        result = db_conn.session.execute(statement).scalars().all()
        return result
