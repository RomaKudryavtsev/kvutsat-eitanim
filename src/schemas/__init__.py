from .base import ma
from .lead import LeadSchema
from .project import ProjectSchema
from .site_settings import SiteSettingsSchema

lead_schema = LeadSchema()
project_schema = ProjectSchema()
multi_project_schema = ProjectSchema(many=True)
site_settings_schema = SiteSettingsSchema()
__all__ = (
    "ma",
    "lead_schema",
    "project_schema",
    "multi_project_schema",
    "site_settings_schema",
)
