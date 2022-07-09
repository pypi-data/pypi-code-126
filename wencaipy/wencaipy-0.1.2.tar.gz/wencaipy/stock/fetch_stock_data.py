from wencaipy.common.fetch_base_wencai import fetch_data_from_wencai

def fetch_stock_new_high(trade_date=None, new_high_period="250"):
    """ new high; history=0 / 250 """
    if (new_high_period == 0)  or (not new_high_period):
        Fields_new_high_query = ["历史新高", "所属申万行业"] 
    else:
        Fields_new_high_query = [f"{new_high_period}日新高","所属申万行业"]
    Fields_new_high = ["股票简称", "股票代码", '最新价', '最新涨跌幅', "所属申万行业"]
    return  fetch_data_from_wencai(trade_date,Fields_new_high_query, Fields_new_high)

if __name__ == "__main__":
    
    print(fetch_stock_new_high())
    
    
