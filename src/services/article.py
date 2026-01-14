from ..models import Article
from ..repos import ArticleRepo
from ..schemas import single_article_schema, multiple_articles_schema


class ArticleService:
    def __init__(self, article_repo: ArticleRepo):
        self.article_repo = article_repo

    def get_article_by_id(self, article_id: int):
        article = self.article_repo.get_article_by_id(article_id)
        if not article:
            raise KeyError(f"Article with id {article_id} not found")
        return single_article_schema.dump(article)

    def get_article_content(self, article_id: int):
        article = self.article_repo.get_article_by_id(article_id)
        if not article:
            raise KeyError(f"Article with id {article_id} not found")
        return article.content

    def get_all_articles(self):
        articles = self.article_repo.get_all_articles()
        return multiple_articles_schema.dump(articles) if articles else []
