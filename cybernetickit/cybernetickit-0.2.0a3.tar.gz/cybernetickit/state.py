from elasticsearch_dsl import GeoShape, Keyword, GeoPoint, Object

from cybernetickit import CoreModel, geo


class State(CoreModel):
    name = Keyword()
    abbr = Keyword()
    fips = Keyword()
    geometry = GeoShape()
    area = Object(geo.Area)
    centroid = GeoPoint()

    class Index:
        name = 'state'
        doc_type = 'state'

    class Meta:
        doc_type = 'state'
