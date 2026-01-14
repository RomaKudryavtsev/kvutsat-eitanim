from flask import Blueprint, jsonify, current_app
from ..services import SiteSettingsService

site_settings_bp = Blueprint("site_settings_api", __name__)


@site_settings_bp.get("/")
def get_site_settings():
    site_settings_service: SiteSettingsService = current_app.site_settings_service
    site_settings = site_settings_service.get_site_settings()
    return jsonify(site_settings), 200
