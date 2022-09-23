from fastapi import FastAPI

from articles.services.article_service import ArticleService
from articles.services.es_service import ElasticsearchService
from configs.config import ConfigProvider
from fn import init_articles

app = FastAPI()

config = ConfigProvider()
es_service = ElasticsearchService(**config.provide_elasticsearch())
article_service = ArticleService(es_service)

# init
es_service.delete_index("test")
init_articles(article_service)


@app.get("/{word}")
async def get_word_stats(word: str):
    stats = article_service.get_word_stats(word)
    return stats
