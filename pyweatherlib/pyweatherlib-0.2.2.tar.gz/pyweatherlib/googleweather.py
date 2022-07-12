from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 " \
             "Safari/537.36 "
# US english
LANGUAGE = "en-US,en;q=0.5"


def weather_data():
    url = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get(url)
    # create a new soup
    soup = bs(html.text, "html.parser")
    # store all results on this dictionary
    result = {'region': soup.find("div", attrs={"id": "wob_loc"}).text,
              'temp_now': soup.find("span", attrs={"id": "wob_tm"}).text,
              'dayhour': soup.find("div", attrs={"id": "wob_dts"}).text,
              'weather_now': soup.find("span", attrs={"id": "wob_dc"}).text,
              'precipitation': soup.find("span", attrs={"id": "wob_pp"}).text,
              'humidity': soup.find("span", attrs={"id": "wob_hm"}).text,
              'wind': soup.find("span", attrs={"id": "wob_ws"}).text}
    # extract region
    # extract temperature now
    # get the day and hour now
    # get the actual weather
    # get the precipitation
    # get the % of humidity
    # extract the wind
    # get next few days' weather
    next_days = []
    days = soup.find("div", attrs={"id": "wob_dp"})
    for day in days.findAll("div", attrs={"class": "wob_df"}):
        # extract the name of the day
        day_name = day.findAll("div")[0].attrs['aria-label']
        # get weather status for that day
        weather = day.find("img").attrs["alt"]
        temp = day.findAll("span", {"class": "wob_t"})
        # maximum temparature in Celsius, use temp[1].text if you want fahrenheit
        max_temp = temp[0].text
        # minimum temparature in Celsius, use temp[3].text if you want fahrenheit
        min_temp = temp[2].text
        next_days.append({"name": day_name, "weather": weather, "max_temp": max_temp, "min_temp": min_temp})
    # append to result
    result['next_days'] = next_days
    return result


def next_days_forecast(data, dashes=10, style="-"):
    for dayweather in data["next_days"]:
        print(style * dashes, dayweather["name"], style * dashes)
        print("Description:", dayweather["weather"])
        print(f"Max temperature: {dayweather['max_temp']}°C")
        print(f"Min temperature: {dayweather['min_temp']}°C")


def get_region(result):
    return result["region"]


def temperature(result):
    return result['temp_now']


def description(result):
    return result['weather_now']


def precipitation(result):
    return result["precipitation"]


def humidity(result):
    return result["humidity"]


def wind(result):
    return result["wind"]


if __name__ == "__main__":
    try:
        x = datetime.now()
        # get data
        data = weather_data()
        # print data
        print("Weather for:", get_region(data))
        print("Date: {}".format(x.strftime("%d-%b-%Y")))
        print("Time: {}".format(x.strftime("%I:%M %p")))
        print(f"Temperature: {temperature(data)}°C")
        print("Description:", description(data))
        print("Precipitation:", precipitation(data))
        print("Humidity:", humidity(data))
        print("Wind:", wind(data))
        next_days_forecast(data)
    except:
        print("You're not connected to internet.")
