from elasticsearch_dsl import Keyword, GeoShape, GeoPoint, Nested, Object, Double, Integer, Text, InnerDoc
from cybernetickit import CoreModel, geo


class SubjectScore(InnerDoc):
    metric = Keyword()
    value = Double()
    type = Keyword()


class District(InnerDoc):
    code = Keyword()
    name = Text()
    state = Keyword()


class SchoolDistrictPercolate(geo.GeoPercolate):
    state = Keyword()

    class Index:
        name = 'perc'
        doc_type = 'perc'

    class Meta:
        doc_type = 'perc'


class SchoolDistrict(CoreModel):
    name = Keyword()
    state = Keyword()
    year = Keyword()
    geoid = Keyword()
    lowest_grade = Keyword()
    highest_grade = Keyword()
    geometry = GeoShape()
    centroid = GeoPoint()
    kind = Keyword()
    area = Object(geo.Area)

    class Index:
        name = 'school.district'
        doc_type = 'school.district'

    class Meta:
        doc_type = 'school.district'


class AssessmentScore(CoreModel):
    year = Keyword()
    state = Keyword()
    subgroup = Keyword()
    participation_rate = Double()
    total_tests = Integer()
    science = Object(SubjectScore)
    english = Object(SubjectScore)
    math = Object(SubjectScore)
    reading = Object(SubjectScore)
    composite = Object(SubjectScore)
    type = Keyword()
    district = Object(District)
    fact = Nested(properties={
        'name': Text(),
        'value': Double(),
        'type': Keyword()
    })

    class Index:
        name = 'assessment'
        doc_type = 'assessment'

    class Meta:
        doc_type = 'assessment'

    def add_fact(self, fact_title, fact_value, fact_type='numeric'):
        self.fact.append({
            'title': fact_title,
            'type': fact_type,
            'value': fact_value
        })
