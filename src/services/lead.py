from ..models import Lead
from ..repos import LeadRepo
from ..schemas import lead_schema
from .utils import transactional


class LeadService:
    def __init__(self, lead_repo: LeadRepo):
        self.lead_repo = lead_repo

    @transactional
    def create_lead(self, req_body) -> dict:
        lead_dto = lead_schema.load(req_body)
        lead = Lead(**lead_dto)
        created_lead = self.lead_repo.create_lead(lead)
        return lead_schema.dump(created_lead)
