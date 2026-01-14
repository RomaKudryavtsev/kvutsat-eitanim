from ..models import SiteSettings
from .base import ma


# IMPORTANT: Schemas are pure dtos. If additional fields are needed, they are just declared here but all the logic stays in the service layer.
class SiteSettingsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SiteSettings
