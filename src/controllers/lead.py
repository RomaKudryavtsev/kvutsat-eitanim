from flask import Blueprint, jsonify, current_app, request
from ..services import LeadService

lead_bp = Blueprint("lead_api", __name__)


@lead_bp.post("/")
def save_lead():
    lead_service: LeadService = current_app.lead_service
    req_body = request.get_json()
    created_lead = lead_service.create_lead(req_body)
    return jsonify(created_lead), 200
