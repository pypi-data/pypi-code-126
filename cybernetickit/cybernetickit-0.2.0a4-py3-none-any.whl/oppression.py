from elasticsearch_dsl import Object, InnerDoc
from elasticsearch_dsl import Keyword, Date, Integer, GeoPoint, Boolean
from cybernetickit import CoreModel


class Duration(InnerDoc):
    length = Integer()
    units = Keyword()  # hours, minutes, days


class Microaggression(CoreModel):
    type = Keyword()  # race, sexuality, gender, age, intersection
    racism = Boolean()
    sexism = Boolean()
    ageism = Boolean()
    colorism = Boolean()
    xenophobia = Boolean()
    antilgbtqi = Boolean()
    location = GeoPoint()
    at = Date(default_timezone='UTC')
    duration = Object(Duration)
    visibility = Keyword()  # private, public
    source = Keyword()  # online, person, organization
    reporter = Keyword()  # anonymous or user's email

    class Index:
        name = 'microaggression'
        doc_type = 'microaggression'

    class Meta:
        doc_type = 'microaggression'
