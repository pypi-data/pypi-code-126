from elasticsearch_dsl import Keyword, GeoShape, GeoPoint, Object, Boolean

from cybernetickit import CoreModel, geo


class Tract(CoreModel):
    name = Keyword()
    name_full = Keyword()
    fips = Keyword()
    ce = Keyword()
    state = Keyword()
    county = Keyword()
    geometry = GeoShape()
    centroid = GeoPoint()
    area = Object(geo.Area)
    opportunityzone = Boolean()

    class Index:
        name = 'tract'
        doc_type = 'tract'

    class Meta:
        doc_type = 'tract'
