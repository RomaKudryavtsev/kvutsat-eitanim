from flask import Blueprint, current_app, send_from_directory

uploads_bp = Blueprint("uploads_api", __name__)


@uploads_bp.get("/img/<filename>")
def get_image(filename):
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], filename)
