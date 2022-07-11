"""
sql rendering functions
"""
import re
from typing import List, Dict, Any

from rasgotransforms.render import RasgoEnvironment
import pandas as pd

from pyrasgo.schemas.dw_operation import Operation, OperationCreate
from pyrasgo.schemas.transform import Transform
from pyrasgo.utils import naming
from pyrasgo.constants import SOURCE_TABLE_ARG_NAME

__all__ = ['operations_as_cte', 'offline_operations_as_cte']


def operation_as_subquery(source_code: str, source_table: str, arguments: Dict[str, Any], running_sql: str = '') -> str:
    from pyrasgo.api import Read

    def run_query(query) -> pd.DataFrame:
        query = f'{running_sql} {query}'
        result = Read().data_warehouse.query_into_dataframe(query)
        return result

    def get_columns(table: str) -> Dict[str, str]:
        if running_sql:
            return Read().data_warehouse.get_schema(f"{running_sql} SELECT * FROM {table}")
        else:
            return Read().data_warehouse.get_schema(table)

    env = RasgoEnvironment(run_query=run_query)
    return env.render(
        source_code=source_code,
        source_table=source_table,
        arguments=arguments,
        override_globals={'get_columns': get_columns},
    )


def offline_operations_as_cte(operations: List[OperationCreate], transforms: List[Transform]) -> str:
    if operations:
        transforms = {t.id: t.sourceCode for t in transforms}
        sql = ''
        last_op = operations[0].operation_args[SOURCE_TABLE_ARG_NAME]
        for i in range(len(operations)):
            operation_sql = operation_as_subquery(
                source_code=transforms[operations[i].transform_id],
                source_table=last_op,
                running_sql=sql,
                arguments=operations[i].operation_args.copy(),
            )
            last_op = operations[i].table_name
            sql += 'WITH ' if i == 0 else ', '
            sql += f"{operations[i].table_name} as (\n{operation_sql}\n)"
        sql += f' SELECT * FROM {last_op}'
        return sql


def operations_as_cte(
    operations: List[Operation],
) -> str:
    """
    Returns a nested CTE statement to render this op set as a CTE
    """
    # Handle single transform chains, we already have the SQL
    if len(operations) == 1:
        return operations[0].operation_sql

    # Handle multi-transform chains
    operation_list = []
    # Need to replace old FQTNs with CTE aliases
    fqtn_mapping = {}
    for operation in operations:
        # create new aliases to replace old FQTNs with
        alias = operation.dw_table.table_name or naming.random_table_name()
        fqtn_mapping[operation.dw_table.fqtn] = alias

        op_sql = operation.operation_sql

        # replace all instances of generated FQTNs with CTE aliases
        for fqtn, alias in fqtn_mapping.items():
            op_sql = op_sql.replace(fqtn, alias)

        # if final op, we're done. join ops and leave last one alone
        # Final op itself might be a CTE, remove the WITH and slap it on the end of this chain
        if operation == operations[-1]:
            return 'WITH {}{}'.format(', \n'.join(operation_list), collapse_cte(op_sql))

        operation_list.append(f'{alias} AS (\n{op_sql}\n) ')


def collapse_cte(sql: str) -> str:
    """
    Returns a collapsed CTE if the sql itself is already a CTE (starts with "with")
    """
    return re.sub(r'^(WITH)\s', ', ', sql, 1, flags=re.IGNORECASE)
