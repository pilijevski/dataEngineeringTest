import dataclasses

from articles.article import Article
from articles.services.es_service import ElasticsearchService


class ArticleService:
    def __init__(self, es_service: ElasticsearchService):
        self.es = es_service

    def store_article(self, article: Article):
        self.es.add_document(dataclasses.asdict(article))
