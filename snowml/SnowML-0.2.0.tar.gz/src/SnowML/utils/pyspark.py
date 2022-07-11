from pyspark.sql import functions as f


def explode_map_column(df, column, prefix=None, func=None, func_args=None):
    """Explode a map column by replacing it with a new columns per key
    :param pyspark.sql.DataFrame df: the dataframe with the column to explode
    :param str column: the target column to explode, it should be a one level map
    :param str prefix: (optional) an optional prefix for the aliases
    :param function func: (optional) a pyspark column function to apply to each value.
        See :numref:`func-example` for an example on perspective scores.
    :param dict func_args: (optional) a dictionary with optional arguments for func
    :return: the df with exploded column
    :rtype: pyspark.sql.DataFrame

    :Example:
    ... code-block:: python
       :name: func-example

       func = lambda col: f.regexp_replace(col, '%', '').astype('integer')/100
    """
    if prefix is None:
        prefix = column + '_'
    if func_args is None:
        func_args = {}

    map_keys = df.select(f.explode(f.map_keys(column))).distinct().rdd.flatMap(lambda row: row).collect()

    if func is not None:
        exploded_columns = map(lambda map_key: func(f.col(column).getItem(map_key), *func_args).alias(prefix + map_key),
                               map_keys)
    else:
        exploded_columns = map(lambda map_key: f.col(column).getItem(map_key).alias(prefix + map_key), map_keys)

    selected_columns = []
    for col in df.columns:
        if col == column:
            for exploded_column in exploded_columns:
                selected_columns.append(exploded_column)
        else:
            selected_columns.append(col)

    return df.select(selected_columns)
