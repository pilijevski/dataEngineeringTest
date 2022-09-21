import logging

from elasticsearch import Elasticsearch


class ElasticsearchService:
    def __init__(self, host: str, port: int, username: str, password: str):
        self.host = host
        self.port = port

        self.es = Elasticsearch([{'scheme': 'http', 'host': '0.0.0.0', 'port': 9200}],
                                basic_auth=(username, password))

    def connect(self):
        if not self.es.ping(human=True):
            logging.error(f"Elasticsearch endpoint {self.host}:{self.port} is unreachable.")

    def add_document(self, document):
        self.es.index(index="test", document=document)

    def get_term_statistics(self, term: str):
        result = self.es.termvectors(index="test", doc={"text": term}, term_statistics=True, payloads=True,
                                     positions=True)
        return result.body['term_vectors']['text']['terms'][term]
