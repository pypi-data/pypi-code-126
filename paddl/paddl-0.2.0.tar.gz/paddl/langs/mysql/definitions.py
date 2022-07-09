from pyparsing import (
    Word, Optional, alphas, alphanums, nums,
    MatchFirst, OneOrMore, ZeroOrMore, Group,
    CaselessKeyword, oneOf
)
from .keywords import *


def COMMENT(string):
    return Optional(CaselessKeyword("COMMENT") + string)


reference_definition = (
    REFERENCES + tbl_name + "(" + key_part___ + ")"
    # Optional(MatchFirst([MATCH_FULL, MATCH_PARTIAL, MATCH_SIMPLE]))
    # ON_DELETE reference_option
    # ON_UPDATE reference_option
)
# column_definition: {
column_definition = MatchFirst((
    # data_type [NOT NULL | NULL] [DEFAULT {literal | (expr)} ]
    data_type + NULLY + DEFAULT,
    # [VISIBLE | INVISIBLE]
    # [AUTO_INCREMENT] [UNIQUE [KEY]] [[PRIMARY] KEY]
    # [COMMENT 'string']
    # [COLLATE collation_name]
    # [COLUMN_FORMAT {FIXED | DYNAMIC | DEFAULT}]
    # [ENGINE_ATTRIBUTE [=] 'string']
    # [SECONDARY_ENGINE_ATTRIBUTE [=] 'string']
    # [STORAGE {DISK | MEMORY}]
    # [reference_definition]
    # [check_constraint_definition]
    # | data_type
    data_type +\
    # [COLLATE collation_name]
    # [GENERATED ALWAYS] AS (expr)
    # [VIRTUAL | STORED] [NOT NULL | NULL]
    # [VISIBLE | INVISIBLE]
    # [UNIQUE [KEY]] [[PRIMARY] KEY]
    # [COMMENT 'string']
    COMMENT(string) +\
    # [reference_definition]
    reference_definition
    # [check_constraint_definition]
    # }
))




# create_definition: {
#     col_name column_definition
#   | {INDEX | KEY} [index_name] [index_type] (key_part,...)
#       [index_option] ...
#   | {FULLTEXT | SPATIAL} [INDEX | KEY] [index_name] (key_part,...)
#       [index_option] ...
#   | [CONSTRAINT [symbol]] PRIMARY KEY
#       [index_type] (key_part,...)
#       [index_option] ...
#   | [CONSTRAINT [symbol]] UNIQUE [INDEX | KEY]
#       [index_name] [index_type] (key_part,...)
#       [index_option] ...
#   | [CONSTRAINT [symbol]] FOREIGN KEY
#       [index_name] (col_name,...)
#       reference_definition
CONSTRAINT_FOREIGN_KEY = (
    Optional(CaselessKeyword("CONSTRAINT") + Word(alphanums_)("symbol")) +
    CaselessKeyword("FOREIGN KEY") + Optional(Word(alphanums_))("index_name") +
    "(" + OneOrMore(Word(alphanums_))("col_names") + ")" +
    reference_definition
)
#   | check_constraint_definition
# }

column_definition = MatchFirst((
    col_name + data_type + NULLY + DEFAULT,
    CONSTRAINT_FOREIGN_KEY,  # FK first for specificity
))

# should be able to mix up order of rows
create_definition = '(' + \
                    OneOrMore(Group(
                        column_definition.ignore(',')
                    ))("columns") + \
                    ')'
# ZeroOrMore(CONSTRAINT_FOREIGN_KEY)("fks") + \

table_options = Optional(CaselessKeyword("IOU-FEATURE"))  # Optional(Word(alphanums).ignore("=") + Word(alphanums))

partition_options = Optional(CaselessKeyword("PARITION"))