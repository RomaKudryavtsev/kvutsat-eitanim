from ..models import SiteSettings
from .base import ma


class SiteSettingsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SiteSettings
