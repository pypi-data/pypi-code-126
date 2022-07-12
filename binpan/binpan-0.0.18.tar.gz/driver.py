import binpan
from time import time
from tqdm import tqdm

start_time = int(time())

redis_client = binpan.redis_cosummer(ip='192.168.89.242')
tick_interval = '5m'

all_keys = binpan.handlers.redis_fetch.fetch_keys(redisClient=redis_client,
                                                  filter_tick_interval=tick_interval)

all_data = binpan.handlers.redis_fetch.fetch_list_filter_query(redisClient=redis_client,
                                                               coin_filter='BUSD',
                                                               tick_interval_filter=tick_interval)
dfs = {}
for ticker in tqdm(all_keys):
    ticker_data = all_data[ticker]
    symbol = ticker.split('@')[0].upper()
    tick_interval_ = ticker.split('@')[1]
    df = binpan.handlers.redis_fetch.redis_klines_parser(json_list=ticker_data,
                                                         symbol=symbol,
                                                         tick_interval=tick_interval_)
    dfs[symbol] = df

end_time = int(time())
print(f"Elapsed seconds: {end_time - start_time}")
pass
