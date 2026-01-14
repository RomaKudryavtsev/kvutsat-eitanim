from .base import ma


class LeadSchema(ma.Schema):
    name = ma.String(required=True)
    email = ma.String(required=True)
    phone = ma.String(required=False, allow_none=True)
    message = ma.String(required=False, allow_none=True)
