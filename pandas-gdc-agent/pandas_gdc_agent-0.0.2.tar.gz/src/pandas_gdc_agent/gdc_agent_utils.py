import pandas as pd
from pandas.api.types import is_numeric_dtype, is_string_dtype

# This filters data based on the `where_dict`
def filterData(df:pd.DataFrame, where_dict: dict):
    if where_dict['type'] == "and":
        if where_dict['expressions'] == []:
            return df
        for exp in where_dict['expressions']:
            df = filterData(df, exp)
        return df
    elif where_dict['type'] == "or":
        dfLst = []
        for exp in where_dict['expressions']:
            dfClone = df.copy(deep=True)
            dfLst.append(filterData(dfClone, exp))
        return pd.concat(dfLst)
    elif where_dict['type'] == "not":
        dfClone = df.copy(deep=True)
        exp = where_dict['expression']
        pos_df = filterData(dfClone, exp)
        return df.drop(pos_df.index)
    elif where_dict['type'] == "binary_op":
        c_name = where_dict['column']['name']
        val = where_dict['value']['value']
        if where_dict['operator'] == "equal":
            return df.loc[df[c_name] == val]
        elif where_dict['operator'] == "less_than":
            return df.loc[df[c_name] < val]
        elif where_dict['operator'] == "less_than_or_equal":
            return df.loc[df[c_name] <= val]
        elif where_dict['operator'] == "greater_than":
            return df.loc[df[c_name] > val]
        elif where_dict['operator'] == "greater_than_or_equal":
            return df.loc[df[c_name] >= val]
        else:
            return "Operator " + where_dict['operator'] + "not supported yet"
    elif where_dict['type'] == "binary_arr_op":
        c_name = where_dict['column']['name']
        vals = where_dict['values']
        if where_dict['operator'] == "in":
            return df[df[c_name].isin(vals)]
        else:
            return "Operator " + where_dict['operator'] + "not supported yet"
    else:
        return "Expression type " + where_dict['type'] + "not supported yet"

# This orders the dataframe based on the `order_dict`
def orderData(df:pd.DataFrame, order_dict: dict):
    c_name = order_dict['column']
    if order_dict['ordering'] == "asc":
        return df.sort_values(by=c_name)
    elif order_dict['ordering'] == "desc":
        return df.sort_values(by=c_name, ascending=False)
    else:
        return "order type " + order_dict['ordering'] + "not supported yet"

# This will generate query list
def getQuery(df:pd.DataFrame, query_request: dict, table_relationships: list, agent_dfs: dict):
    df = filterData(df, query_request['where'])
    if 'order_by' in query_request:
        for ord in query_request['order_by']:
            df = orderData(df, ord)
    if isinstance(df, pd.DataFrame):
        datas = df.to_dict(orient='records')
        st = query_request['offset'] if 'offset' in query_request else 0
        end = st + query_request['limit'] if 'limit' in query_request else len(datas)
        datas = datas[st:end]
        all_data  = []
        for d in datas:
            e = dict()
            for (f_name, val) in query_request['fields'].items():
                if val["type"] == "column":
                    c_name = val['column']
                    e[f_name] = d[c_name]
                elif val["type"] == "relationship":
                    rel_name = val["relationship"]
                    rel_dict = getRelationship(table_relationships, rel_name)
                    rel_df_all = agent_dfs[rel_dict["target_table"]]
                    rel_df = getRelationshipDataFrame(d, rel_df_all, rel_dict)
                    rel_data = getQuery(rel_df, val["query"], table_relationships, agent_dfs)
                    e[f_name] = rel_data
            all_data.append(e)
        return all_data
    elif isinstance(df, str):
        return df
    else:
        raise "some unexpected error occured."

# This returns the relationship dictionary based on relationship name
def getRelationship(table_relationships:list, rel_name):
    for rel in table_relationships:
        if rel_name in rel["relationships"]:
            return rel["relationships"][rel_name]
    raise "relationship with name " + rel_name + " not found in table relations."

# This filters out the relationship dataframe based on the current data
def getRelationshipDataFrame(curr_data: dict, rel_df: pd.DataFrame, rel_dict: dict):
    column_mapping = rel_dict["column_mapping"]
    if len(column_mapping) != 1:
        raise "column mappings incorrect for relationship"
    for (fromCol, toCol) in column_mapping.items():
        match_val = curr_data[fromCol]
        return rel_df.loc[rel_df[toCol] == match_val]

# This is just for serializing the dtype of dataframe while building `schema.json`
#      TODO: add more dtypes
def serializeDtype(dtype):
    if is_numeric_dtype(dtype):
        return "number"
    elif is_string_dtype(dtype):
        return "string"
    else:
        raise "unknown datatype" + str(dtype)