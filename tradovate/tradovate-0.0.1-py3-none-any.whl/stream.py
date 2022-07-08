import asyncio, ssl, requests, math, os, json, logging, pytz, redis, statistics, numpy, time
from datetime import date, datetime, timedelta
import pandas as pd
import pandas_ta as ta
from websocket import create_connection, WebSocketConnectionClosedException
from . import auth

ws = create_connection("wss://demo.tradovateapi.com/v1/websocket", sslopt={"cert_reqs": ssl.CERT_NONE})

def run_real_time(tickers):
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    task = loop.create_task(connect_stream(tickers))
    try:
        loop.run_until_complete(task)
    except SystemExit:
        print("caught SystemExit!")
        task.exception()
        raise
    finally:
        loop.close()

async def connect_stream(tickers):
    token = auth.access_token()

    print(">>>>>>>",token['mdAccessToken'])
    subscribe = {
        'eventName': 'subscribe',
        'authorization': token['mdAccessToken'],
        'eventData': {
            'thresholdLevel': 5,
            'tickers': tickers
        }
    }



    ws.send("authorize\n1\n\n"+token['mdAccessToken'])
    while True:
        try:
            print(">>>>>", ws.recv())
            connect_handler(json.loads(ws.recv()))
        except WebSocketConnectionClosedException as e:
            print("Failed to receive: %s" % (e))

def connect_handler(msg):
    print(msg)

    print(">>>>>>>>>>>>>>>")



def price_handler(msg):

    body = {}
    if msg['messageType'] != 'A':
        return
    data = msg['data']
    if data[0] != 'T':
        return
    ticker = data[3]
    close_price = data[9]
    volume = data[10]
    date_time = data[2]
    res_data = {"price": close_price, 'volume': volume, 'change': 0, 'pct': 0, 'datetime': date_time}
    body[ticker] = res_data

    url = os.environ.get('STOCK_API_URI') + "/watchlist/realtime-price"
    headers = {'content-type': 'application/json',
               'accept': 'application/json',
               'authorization': os.environ.get('STOCK_API_KEY')}
    data = json.dumps(body)
    resp = requests.post(url=url, data=data, headers=headers)
    print("realtime-price:", resp)