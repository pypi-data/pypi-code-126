import requests

class Bypass():
  def __init__(self,apikey):
    async def get(url,headers=None,cookie=None,proxies=None):
      if proxies:
        return requests.get(f"http://api.scraperapi.com?api_key={apikey}&url=" + url,cookie=None,headers=headers,proxies=proxies)
      if not proxies:
        return requests.get(f"http://api.scraperapi.com?api_key={apikey}&url=" + url,cookie=cookie,headers=headers)
      
    async def post(url,data,headers=None,cookie=None,proxies=None):
      if proxies:
        return requests.post(f"http://api.scraperapi.com?api_key={apikey}&url=" + url,data=data,cookie=None,headers=headers,proxies=proxies)
      if not proxies:
        return requests.post(f"http://api.scraperapi.com?api_key={apikey}&url=" + url,data=data,cookie=cookie,headers=headers)
      
    async def put(url,headers=None,cookie=None,proxies=None):
      if proxies:
        return requests.put(f"http://api.scraperapi.com?api_key={apikey}&url=" + url,cookie=cookie,headers=headers,proxies=proxies)
      if not proxies:
        return requests.put(f"http://api.scraperapi.com?api_key={apikey}&url=" + url,cookie=cookie,headers=headers)

    async def patch(url,data,headers=None,cookie=None,proxies=None):
      if proxies:
        return requests.patch(f"http://api.scraperapi.com?api_key={apikey}&url=" + url,data=data,cookie=cookie,headers=headers,proxies=proxies)
      if not proxies:
        return requests.patch(f"http://api.scraperapi.com?api_key={apikey}&url=" + url,data=data,cookie=cookie,headers=headers)

    async def delete(url,headers=None,cookie=None,proxies=None):
      if proxies:
        return requests.delete(f"http://api.scraperapi.com?api_key={apikey}&url=" + url,cookie=cookie,headers=headers,proxies=proxies)
      if not proxies:
        return requests.delete(f"http://api.scraperapi.com?api_key={apikey}&url=" + url,cookie=cookie,headers=headers)