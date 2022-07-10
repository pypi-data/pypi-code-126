from wencaipy.common.fetch_base_wencai import fetch_data_from_wencai
from wencaipy.common.wcParameter import QUERY_TYPE
from wencaipy.common.dataToExcel import data_to_excel


def fetch_ths_sector_index():
    """ 同花顺板块指数 :764 同花顺行业指数 同花顺特色指数  同花顺概念指数 同花顺地域指数"""
    Fields_Query = ["同花顺板块指数"]
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_Query,query_type=QUERY_TYPE().index)
    data_to_excel(df, "ths_all_index")
    return df

def fetch_ths_industry_level3_index():
    """ 同花顺板块指数 :764 同花顺行业指数 同花顺特色指数  同花顺概念指数 同花顺地域指数"""
    Fields_Query = ["同花顺板块指数","三级行业"]
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_Query,query_type=QUERY_TYPE().index)
    data_to_excel(df, "ths_level3_index")
    return df

def fetch_ths_area_index():
    """ 同花顺板块指数 :764 同花顺行业指数 同花顺特色指数  同花顺概念指数 同花顺地域指数"""
    Fields_Query = ["同花顺板块指数","同花顺地域指数"]
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_Query,query_type=QUERY_TYPE().index)
    data_to_excel(df, "ths_area_index")
    return df

def fetch_ths_concept_index():
    """ 同花顺板块指数 :  同花顺概念指数 """
    Fields_Query = ["同花顺板块指数","同花顺概念指数"]
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_Query,query_type=QUERY_TYPE().index)
    data_to_excel(df, "ths_concept_index")
    return df


if __name__ == "__main__":
    
    print(fetch_ths_sector_index())
    print(fetch_ths_industry_level3_index())
    print(fetch_ths_area_index())
    print(fetch_ths_concept_index())