import logging

from elasticsearch import Elasticsearch
from tenacity import retry, stop_after_attempt, wait_fixed


# > This class is used to connect to an Elasticsearch cluster and perform various operations on it
class ElasticsearchService:
    def __init__(self, host: str, port: int, username: str, password: str, scheme: str):
        self.host = host
        self.port = port

        self.es = Elasticsearch([{'scheme': scheme, 'host': host, 'port': 9200}],
                                basic_auth=(username, password))
        self.connect()

    @retry(reraise=True,
           stop=stop_after_attempt(5),
           wait=wait_fixed(5))
    def connect(self):
        """
        Verifies the connection to Elasticsearch.
        If the Elasticsearch endpoint is unreachable, log an error and raise a ConnectionError
        """
        if not self.es.ping(human=True):
            logging.error(f"Elasticsearch endpoint {self.host}:{self.port} is unreachable.")
            raise ConnectionError

    def add_document(self, document):
        self.es.index(index="test", document=document)

    def delete_index(self,index):
        self.es.options(ignore_status=[400,404]).indices.delete(index=index)

    def get_term_statistics(self, term: str):
        result = self.es.termvectors(index="test", doc={"text": term}, term_statistics=True, payloads=True,
                                     positions=True)
        return result.body['term_vectors']['text']['terms'][term]
