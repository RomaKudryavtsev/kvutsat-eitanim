from .base import ma
from .project import ProjectSchema
from .site_settings import SiteSettingsSchema

project_schema = ProjectSchema()
multi_project_schema = ProjectSchema(many=True)
site_settings_schema = SiteSettingsSchema()
__all__ = ("ma", "site_settings_schema")
