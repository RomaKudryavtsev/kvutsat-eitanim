from flask import Blueprint, request, jsonify, current_app, send_from_directory
import os
from werkzeug.utils import secure_filename

uploads_bp = Blueprint("uploads_api", __name__)


@uploads_bp.post("/img")
def upload_image():
    if "upload" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files["upload"]
    filename = secure_filename(file.filename)
    upload_folder = current_app.config["UPLOAD_FOLDER"]
    file_path = os.path.join(upload_folder, filename)
    file.save(file_path)
    url = f"/static/uploads/{filename}"
    return jsonify({"url": url})


@uploads_bp.get("/img/<filename>")
def get_image(filename):
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], filename)
