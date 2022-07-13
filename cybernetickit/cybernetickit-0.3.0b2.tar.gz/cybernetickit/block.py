from elasticsearch_dsl import Keyword, Integer, Object

from cybernetickit import CoreModel as AliasDocType
from cybernetickit.county import County
from cybernetickit.state import State


class CensusBlock(AliasDocType):
    fips = Keyword()
    state = Object(State)
    county = Object(County)
    tract = Keyword()

    # Totals
    total = Integer()  # P0120001 also P0040001
    male = Integer()  # P0120002
    female = Integer()  # P0120026

    non_hispanic = Integer()  # P0040002
    hispanic = Integer()  # P0040003

    # Non-Hispanic Race Totals
    white = Integer()  # P0070003
    black = Integer()  # P0070004
    native = Integer()  # P0070005
    asian = Integer()  # P0070006
    hawaiian = Integer()  # P0070007
    other = Integer()  # P0070008

    # Hispanic Race Totals
    hispanic_white = Integer()  # P0070010
    hispanic_black = Integer()  # P0070011
    hispanic_native = Integer()  # P0070012
    hispanic_asian = Integer()  # P0070013
    hispanic_hawaiian = Integer()  # P0070014
    hispanic_other = Integer()  # P0070015

    # Race-Gender Breakdowns
    white_male = Integer()  # P012A002 or P012A025
    white_female = Integer()  # P012A026 or P012A049
    black_male = Integer()  # P012B002
    black_female = Integer()  # P012B026
    native_male = Integer()  # P012C002
    native_female = Integer()  # P012C026
    asian_male = Integer()  # P012D002
    asian_female = Integer()  # P012D026
    hawaiian_male = Integer()  # P012E002
    hawaiian_female = Integer()  # P012E026
    other_male = Integer()  # P012F002
    other_female = Integer()  # P012F026

    class Index:
        name = 'block'
        doc_type = 'block'

    class Meta:
        doc_type = 'block'
