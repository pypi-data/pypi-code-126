from .definitions import *
from .keywords import *
from .keywords import _

NOT_CREATE_STATEMENT = Word(alphas)


CREATE = CREATE + TEMPORARY + TABLE + IF_NOT_EXISTS + table_name +\
         create_definition + \
         Optional(';')
         # table_options + \
         # partition_options + \

definition = OneOrMore(Group(CREATE))
