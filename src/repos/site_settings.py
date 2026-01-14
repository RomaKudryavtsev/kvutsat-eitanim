from sqlalchemy import select
from ..models import db_conn, SiteSettings


class SiteSettingsRepo:
    def get_site_settings(self) -> SiteSettings | None:
        statement = select(SiteSettings)
        result = db_conn.session.execute(statement).scalar()
        return result
