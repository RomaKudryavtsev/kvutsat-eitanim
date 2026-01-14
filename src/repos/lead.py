from ..models import Lead, db_conn


class LeadRepo:
    def create_lead(self, lead: Lead) -> Lead:
        db_conn.session.add(lead)
        db_conn.session.commit()
        db_conn.session.refresh(lead)
        return lead
