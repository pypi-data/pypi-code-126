import requests

class bypass(apikey):
  global apikey
  async def get(url,headers=None,cookie=None,proxies=None):
    if proxies:
      requests.get(f"http://api.scraperapi.com?api_key={apikey}&url=" + url,cookie=None,headers=headers,proxies=proxies)
    if not proxies:
      requests.get(f"http://api.scraperapi.com?api_key={apikey}&url=" + url,cookie=cookie,headers=headers)
      
  async def post(url,data,headers=None,cookie=None,proxies=None):
    if proxies:
      requests.post(f"http://api.scraperapi.com?api_key={apikey}&url=" + url,data=data,cookie=None,headers=headers,proxies=proxies)
    if not proxies:
      requests.post(f"http://api.scraperapi.com?api_key={apikey}&url=" + url,data=data,cookie=cookie,headers=headers)
      
  async def put(url,headers=None,cookie=None,proxies=None):
    if proxies:
      requests.put(f"http://api.scraperapi.com?api_key={apikey}&url=" + url,cookie=cookie,headers=headers,proxies=proxies)
    if not proxies:
      requests.put(f"http://api.scraperapi.com?api_key={apikey}&url=" + url,cookie=cookie,headers=headers)

  async def patch(url,data,headers=None,cookie=None,proxies=None):
    if proxies:
      requests.patch(f"http://api.scraperapi.com?api_key={apikey}&url=" + url,data=data,cookie=cookie,headers=headers,proxies=proxies)
    if not proxies:
      requests.patch(f"http://api.scraperapi.com?api_key={apikey}&url=" + url,data=data,cookie=cookie,headers=headers)

  async def delete(url,headers=None,cookie=None,proxies=None):
    if proxies:
      requests.delete(f"http://api.scraperapi.com?api_key={apikey}&url=" + url,cookie=cookie,headers=headers,proxies=proxies)
    if not proxies:
      requests.delete(f"http://api.scraperapi.com?api_key={apikey}&url=" + url,cookie=cookie,headers=headers)