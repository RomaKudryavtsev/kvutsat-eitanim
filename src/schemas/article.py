from ..models import Article
from .base import ma


class ArticleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Article
