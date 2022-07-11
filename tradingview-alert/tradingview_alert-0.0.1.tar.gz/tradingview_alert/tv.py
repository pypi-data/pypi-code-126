import requests

def tv_data(sessionid):
    cookies = {'sessionid': sessionid}
    headers = {'referer': 'https://in.tradingview.com/'}
    params = {'log_username': 'gourav', 'log_method': 'list_events', }
    data = '{"m":"list_events","p":{"sym":null,"res":null,"inc_cross_int":true}}'
    response = requests.post('https://alerts.tradingview.com/alerts/', params=params, cookies=cookies, headers=headers,data=data)
    pre = response.json()['p']['events']
    return pre


