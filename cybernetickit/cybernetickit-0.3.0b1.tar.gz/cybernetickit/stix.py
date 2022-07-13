from elasticsearch_dsl import Text, Keyword, Object, InnerDoc, Date

from cybernetickit import CoreModel


class RequiredCommonProperties(InnerDoc):
    type = Keyword() # From STIX 2.1: type=='report'
    spec_version = Keyword()
    id = Keyword()
    created = Keyword()
    modified = Keyword()



class Source(InnerDoc):
    name = Text()
    url = Keyword()


class Report(CoreModel):
    stix_rcp = Object(RequiredCommonProperties)
    name = Text()
    description = Text()
    report_types = Keyword(multi=True) # From STIX 2.1 report-type-ov + ours
    published = Date()
    object_refs = Keyword(multi=True)
    uid = Keyword()
    url = Keyword()
    source = Object(Source)
    locality = Keyword(multi=True) # Must match datasource's locality vocab
    last_revision = Date()

    class Index:
        name = 'stix'
