from fastapi import FastAPI

from articles.services.article_service import ArticleService
from articles.services.es_service import ElasticsearchService
from fn import init_articles

app = FastAPI()
es_service = ElasticsearchService("localhost", 9200, "elasticsearch", "elasticsearchpassword")
article_service = ArticleService(es_service)

# init
es_service.delete_index("test")
init_articles(article_service)


@app.get("/{word}")
async def get_word_stats(word: str):
    stats = article_service.get_word_stats(word)
    return stats
