from typing import List
from elasticsearch_dsl import Text, Keyword, Object, InnerDoc, Date

from cybernetickit import CoreModel


class RequiredCommonProperties(InnerDoc):
    type: str = Keyword() # From STIX 2.1: type=='report'
    spec_version: str = Keyword()
    id: str = Keyword()
    created = Keyword()
    modified = Keyword()



class Source(InnerDoc):
    name: str = Text()
    url: str = Keyword()


class Report(CoreModel):
    stix_rcp = Object(RequiredCommonProperties)
    name: str = Text()
    description: str = Text()
    report_types: List[str] = Keyword(multi=True) # From STIX 2.1 report-type-ov + ours
    published = Date()
    object_refs = Keyword(multi=True)
    uid: str = Keyword()
    url: str = Keyword()
    source = Object(Source)
    locality: List[str] = Keyword(multi=True) # Must match datasource's locality vocab
    last_revision = Date()

    class Index:
        name = 'stix'
