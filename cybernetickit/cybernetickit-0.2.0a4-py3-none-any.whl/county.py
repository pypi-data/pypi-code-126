from elasticsearch_dsl import Keyword, GeoShape, GeoPoint, Object, Text

from cybernetickit import CoreModel, geo


class County(CoreModel):
    name = Text()
    name_full = Text()
    fips = Keyword()
    state = Keyword()
    geometry = GeoShape()
    centroid = GeoPoint()
    area = Object(geo.Area)

    class Index:
        name = 'county'
        doc_type = 'county'

    class Meta:
        doc_type = 'county'
