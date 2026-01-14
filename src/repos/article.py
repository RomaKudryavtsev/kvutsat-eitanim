from sqlalchemy import select
from ..models import db_conn, Article


class ArticleRepo:
    def get_article_by_id(self, article_id: int) -> Article | None:
        statement = select(Article).where(Article.id == article_id)
        result = db_conn.session.execute(statement).scalar()
        return result

    def get_all_articles(self) -> list[Article]:
        statement = select(Article)
        result = db_conn.session.execute(statement).scalars().all()
        return result
