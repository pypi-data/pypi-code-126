from elasticsearch_dsl import Keyword, Date, Text, Boolean
from cybernetickit import CoreModel


class Book(CoreModel):
    id = Keyword()
    isbn = Text()
    title = Text()
    website = Text()
    path = Text()
    date_added = Date()
    format = Keyword()
    deleted = Boolean(default=False)
    filename = Text()
    category = Text()
    tags = Keyword(multi=True)
    level = Keyword()

    class Index:
        name = 'book'

    class Meta:
        doc_type = 'book'
