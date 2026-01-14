from ..models import SiteSettings
from ..repos import SiteSettingsRepo
from ..schemas import site_settings_schema


class SiteSettingsService:
    def __init__(self, site_settings_repo: SiteSettingsRepo):
        self.site_settings_repo = site_settings_repo

    def get_site_settings(self) -> SiteSettings | None:
        site_settings = self.site_settings_repo.get_site_settings()
        if not site_settings:
            return None
        return site_settings_schema.dump(site_settings)
