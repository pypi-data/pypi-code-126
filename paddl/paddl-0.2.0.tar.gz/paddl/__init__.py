import logging
from pyparsing.exceptions import ParseException
from enum import Enum
from .langs.mysql import definition as mysql
from .models import *
from .docs import plantuml as erd


class Language(Enum):
    MYSQL = 'mysql'


PARSERS = {
    Language.MYSQL: mysql
}


def clean(ddl):
    return ddl.replace('`', '')


def table(result):
    """
    :param result: pyparse parseString result
    :return: paddl.Schema
    """
    columns = []
    nts = []
    cont = 0
    for col in result['columns']:
        columns.append(Column(*col[0:3]))

    return Table(name=result['table_name'],
                 columns=columns)


def parse(ddl, engine=Language.MYSQL, strict=False):
    """
    parse SQL DDLs and return Schema objects

    :param ddl: string
    :param engine: db engine, defaults to mysql
    :param strict: should parse strictly or fail
    :return:
    """
    engine = Language(engine)
    ddl = clean(ddl)
    schema = Schema()
    try:
        results = PARSERS[engine].parseString(ddl, parseAll=strict)
        logging.debug(results)
    except ParseException as ex:
        raise Exception(ex.args)\
            # (ex.msg, ex.pstr, ex.parser_element)

    schema.tables = [table(result) for result in results]
    return schema
