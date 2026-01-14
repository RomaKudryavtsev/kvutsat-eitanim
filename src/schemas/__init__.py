from .base import ma
from .article import ArticleSchema
from .site_settings import SiteSettingsSchema

site_settings_schema = SiteSettingsSchema()
single_article_schema = ArticleSchema()
multiple_articles_schema = ArticleSchema(many=True)

__all__ = (
    "ma",
    "site_settings_schema",
    "single_article_schema",
    "multiple_articles_schema",
)
