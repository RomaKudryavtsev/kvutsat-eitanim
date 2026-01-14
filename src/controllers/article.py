from flask import Blueprint, jsonify, current_app, render_template
from ..services import ArticleService

article_bp = Blueprint("article_api", __name__)


@article_bp.get("/")
def get_articles():
    article_service: ArticleService = current_app.article_service
    articles = article_service.get_all_articles()
    return jsonify(articles), 200


@article_bp.get("/<int:article_id>")
def get_article(article_id: int):
    article_service: ArticleService = current_app.article_service
    try:
        article = article_service.get_article_by_id(article_id)
        return jsonify(article), 200
    except KeyError as e:
        return jsonify({"error": str(e)}), 404


@article_bp.get("/page/<int:article_id>")
def get_articles_by_page(article_id: int):
    article_service: ArticleService = current_app.article_service
    content = article_service.get_article_content(article_id)
    return render_template("article.html", content=content)
