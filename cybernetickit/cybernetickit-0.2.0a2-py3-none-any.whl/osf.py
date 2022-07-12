from elasticsearch_dsl import Keyword, Date, Boolean, Text
from cybernetickit import CoreModel


class OSFWork(CoreModel):
    title = Text()
    name = Keyword()
    description = Text()
    affiliations = Text(multi=True)
    contributors = Text(multi=True)
    date = Date()
    date_created = Date()
    date_modified = Date()
    date_published = Date()
    date_updated = Date()
    funders = Text(multi=True)
    hosts = Keyword(multi=True)
    identifiers = Keyword(multi=True)
    justification = Text()
    language = Keyword()
    publishers = Keyword(multi=True)
    retracted = Boolean()
    sources = Keyword(multi=True)
    subjects = Keyword(multi=True)
    tags = Keyword(multi=True)
    types = Keyword(multi=True)
    registration_type = Keyword()
    withdrawn = Boolean()
    catalog = Keyword()

    class Meta:
        index = 'osfwork'
        doc_type = 'osfwork'

    class Index:
        name = 'osfwork'
