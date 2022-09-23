import dataclasses

from ..article import Article
from .es_service import ElasticsearchService


class ArticleService:
    def __init__(self, es_service: ElasticsearchService):
        self.es = es_service

    def store_article(self, article: Article):
        self.es.add_document(dataclasses.asdict(article))

    def get_word_stats(self, term):
        stats = self.es.get_term_statistics(term)
        return {term: {"total_count": stats.get("ttf", 0), "article_count": stats.get('doc_freq', 0)}}
