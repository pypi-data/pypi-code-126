import requests


def internet():
    try:
        if requests.get('https://www.google.com'):
            return True
    except:
        return False


def weather_data(query, api_key):
    res = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?' + query + api_key + '&units=metric')
    return res.json()


def print_weather(result):
    print("Temperature: {}°C ".format(round(result['main']['temp'])))
    print("Feels Like: {}°C".format(round(result['main']['feels_like'])))
    print("Wind Speed: {} m/s".format(result['wind']['speed']))
    print("Humidity: {}%".format(round(result['main']['humidity'])))
    print("Pressure: {} hPa".format(result['main']['pressure']))
    print("Description: {}".format(result['weather'][0]['description']))
    print("Weather: {}".format(result['weather'][0]['main']))


def temperature(result):
    return round(result['main']['temp'])


def feels_like(result):
    return round(result['main']['feels_like'])


def wind_speed(result):
    return result['wind']['speed']


def humidity(result):
    return round(result['main']['humidity'])


def pressure(result):
    return result['main']['pressure']


def description(result):
    return result['weather'][0]['description']


def weather(result):
    return result['weather'][0]['main']


def main():
    # Get your api key from # https://home.openweathermap.org/api_keys
    api_key = '&APPID=' + '54f85bac7eca8e2557da760211b208e4'
    city = input("Enter City: ")
    try:
        query = 'q=' + city
        w_data = weather_data(query, api_key)
        print("Today's {} Weather".format(city))
        print("Temperature: {}°C".format(temperature(w_data)))
        print("Feels Like {}°C".format(feels_like(w_data)))
        print("Wind Speed: {} m/s".format(wind_speed(w_data)))
        print("Humidity: {}%".format(humidity(w_data)))
        print("Pressure: {} hPa".format(pressure(w_data)))
        print("Description: {}".format(description(w_data)))
        print("Weather: {}".format(weather(w_data)))
    except:
        if not internet():
            print("You're not connected to internet.")
        else:
            print('City name not found...')


if __name__ == '__main__':
    main()
