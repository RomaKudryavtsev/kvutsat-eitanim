from flask import Blueprint, jsonify, current_app
from ..services import ProjectService

project_bp = Blueprint("project_api", __name__)


@project_bp.get("/")
def get_projects():
    project_service: ProjectService = current_app.project_service
    projects = project_service.get_all_projects()
    return jsonify(projects), 200


@project_bp.get("/<int:project_id>")
def get_project_by_id(project_id: int):
    project_service: ProjectService = current_app.project_service
    try:
        project = project_service.get_project_by_id(project_id)
        return jsonify(project), 200
    except KeyError as e:
        return jsonify({"error": str(e)}), 404
