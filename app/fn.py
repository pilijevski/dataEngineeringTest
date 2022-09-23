from typing import Dict

import requests

from articles.article import Article
from articles.services.article_service import ArticleService

TITLES = ["Free_Now_(service)",
          "Taxi",
          "Share_taxi",
          "Mobility_as_a_service",
          "Personal_rapid_transit",
          "Ridesharing_company",
          "Hackney_carriage",
          "Vehicle_for_hire",
          "Taximeter",
          "Auto_rickshaw"]

URL = "https://en.wikipedia.org/w/api.php"


def init_articles(article_service: ArticleService):
    """
    It takes an article service, and for each title in the TITLES list, it gets the article from the Wikipedia API,
    transforms it into an article object, and stores it in the article service

    :param article_service: This is the service that we'll use to store the articles
    :type article_service: ArticleService
    """
    for title in TITLES:
        result = get_article(title)
        article = transform_to_article(result)
        article_service.store_article(article)


def get_article(title: str) -> Dict:
    """
    t takes the result of a query to the Wikipedia API and returns article json object

    :param title: The title of the article you want to get
    :type title: str
    :return: A JSON object
    """
    params = {
        "action": "query",
        "prop": "revisions",
        "titles": title,
        "rvprop": "content",
        "rvsection": "0",
        "format": "json"}

    return requests.get(url=URL, params=params).json()


def transform_to_article(result) -> Article:
    """
    Transforms the article to Article Object
    :param result: the result of the API call
    :return: An Article Object.
    """

    pageid = list(result["query"]["pages"].keys())[0]
    page = result["query"]["pages"][pageid]

    return Article(page["pageid"], page["title"], page["revisions"][0]["*"])
