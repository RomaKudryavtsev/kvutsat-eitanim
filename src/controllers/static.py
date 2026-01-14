from flask import Blueprint, send_from_directory, current_app

static_bp = Blueprint("static_api", __name__)


@static_bp.route("/favicon", methods=["GET"])
def get_favicon():
    return send_from_directory(current_app.static_folder, "favicon.ico")
