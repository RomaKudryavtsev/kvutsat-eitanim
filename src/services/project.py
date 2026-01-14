from ..repos import ProjectRepo
from ..schemas import project_schema, multi_project_schema


class ProjectService:
    def __init__(self, project_repo: ProjectRepo):
        self.project_repo = project_repo

    def get_all_projects(self) -> list[dict]:
        projects = self.project_repo.get_all_projects()
        return multi_project_schema.dump(projects)

    def get_project_by_id(self, project_id: int) -> dict | None:
        project = self.project_repo.get_project_by_id(project_id)
        if not project:
            raise KeyError(f"Project with ID {project_id} not found")
        return project_schema.dump(project)
