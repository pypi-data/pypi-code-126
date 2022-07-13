from elasticsearch_dsl import Keyword, Object, InnerDoc
from cybernetickit import CoreModel


REPO_TYPES = [
    {'id': 'socrata', 'name': 'Socrata'},
    {'id': 'ckan', 'name': 'CKAN'},
    {'id': 'dkan', 'name': 'DKAN'},
    {'id': 'opendatasoft', 'name': 'OpenDataSoft'},
    {'id': 'oai', 'name': 'OpenArchives Initiative'},
    {'id': 'arcgis', 'name': 'ArcGIS'},
    {'id': 'web', 'name': 'Generic Web Datasource'},
    {'id': 'frictionless', 'name': 'Frictionless Data'},
    {'id': 'google', 'name': 'Google Datasource'}
]


class VegaSpec(InnerDoc):
    encodings = Object(multi=True)
    mark = Keyword()
    autosize = Object()


class Vega(CoreModel):

    class Index:
        name = 'vega'
        doc_type = 'vega'

    class Meta:
        doc_type = 'vega'

    spec = Object(VegaSpec)
    data = Keyword()
    id = Keyword()
    url = Keyword()
    chooseBy = Keyword()
