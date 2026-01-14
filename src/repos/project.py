from sqlalchemy import select
from ..models import db_conn, Project


class ProjectRepo:
    def get_all_projects(self) -> list[Project]:
        statement = select(Project)
        result = db_conn.session.execute(statement).scalars().all()
        return result

    def get_project_by_id(self, project_id: int) -> Project | None:
        statement = select(Project).where(Project.id == project_id)
        result = db_conn.session.execute(statement).scalar()
        return result
