import json
import requests
from requests.structures import CaseInsensitiveDict
class process():
    def process():
        handle.handle_single_days()
class handle():
    def handle_podcast_analytics():
        data = requesting.get_podcast_analytics()
        vars = json.loads(data)
        kuunteludata = vars['data']
        kuunteludata = str(kuunteludata)
        kuunteludata = kuunteludata.split("],")
        return kuunteludata
    def handle_single_days():
        import datetime
        kuunteludata = handle.handle_podcast_analytics()
        f = open("number.txt", "w")
        f.write("0")
        f.close()
        number = 0
        for data in kuunteludata:
            data = data.replace("{'rows': [[", "")
            data = data.replace(" [", "")
            data = data.replace("]", "")
            data = data.replace("}", "")
            data = data.split(", ")
            date = data[0]
            listens = data[1]
            timestamp = datetime.datetime.fromtimestamp(int(date))
            date = timestamp.strftime('%Y-%m-%d')
            f = open("data.txt", "a")
            f.write(f"{date},{listens};")
            f.close()
            data = f"{date},{listens}"
            e = datetime.datetime.now()
            number += int(listens)
            e = e.strftime("%Y-%m-%d")
            if date == e:
                today_list = listens
        return f"{number}, {today_list}"
class requesting():
    def get_podcast_analytics():
        url = f"https://anchor.fm/api/proxy/v3/analytics/station/webStationId:{settings.webStationId}/plays?timeInterval=86400"
        resp = requests.get(url, headers=settings.headers)
        print(resp.text)
        respo = resp.text.replace(',"columnHeaders":[{"name":"Aika (UTC)","type":"integer","isDateTime":true},{"name":"Kuuntelukerrat","type":"integer"}]', "")
        return respo
class settings():
    f = open("/secrets.txt")
    data = f.read()
    f.close()
    data = data.split(";:")
    cookies = data[0]
    headers = CaseInsensitiveDict()
    headers["authority"] = "anchor.fm"
    headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    headers["accept-language"] = "fi-FI,fi;q=0.9,en;q=0.8"
    headers["cache-control"] = "max-age=0"
    headers["cookie"] = cookies
    headers["dnt"] = "1"
    headers["if-none-match"] = 'W/"231-opsGc+hty/oM+Ct1+IrFUKs684Y"'
    headers["sec-fetch-dest"] = "document"
    headers["sec-fetch-mode"] = "navigate"
    headers["sec-fetch-site"] = "none"
    headers["sec-fetch-user"] = "?1"
    headers["upgrade-insecure-requests"] = "1"
    headers["user-agent"] = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    webStationId = data[1]
    summary_day = 0
process.process()