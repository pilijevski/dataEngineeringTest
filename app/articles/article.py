from dataclasses import dataclass


@dataclass
class Article:
    pageid: str
    title: str
    text: str
