from elasticsearch_dsl import Text, Keyword, Date, Boolean
from elasticsearch_dsl import GeoShape, GeoPoint, Double
from cybernetickit import CoreModel as AliasDocType


class City(AliasDocType):
    name = Keyword()
    fips = Keyword()
    state = Keyword()
    url = Keyword()
    merged = Boolean()
    geometry = GeoShape()
    centroid = GeoPoint()
    area = Double()

    class Index:
        name = 'city'
        doc_type = 'city'

    class Meta:
        doc_type = 'city'


class Department(AliasDocType):
    name = Text()
    url = Keyword()
    locality = Keyword(multi=True)
    city = Keyword()
    state = Keyword()

    class Index:
        name = 'department'
        doc_type = 'department'

    class Meta:
        doc_type = 'department'


class Commission(AliasDocType):
    name = Keyword()
    url = Keyword()
    locality = Keyword(multi=True)
    city = Keyword()
    state = Keyword()

    class Index:
        name = 'commission'
        doc_type = 'commission'

    class Meta:
        doc_type = 'commission'


class Contract(AliasDocType):
    id = Keyword()
    contractor = Keyword()
    buyer = Keyword()
    department = Keyword()
    expiration = Date()
    city = Keyword()
    state = Keyword()

    class Index:
        name = 'contract'
        doc_type = 'contract'

    class Meta:
        doc_type = 'contract'
