import requests

class Weather:
    """
    Create a Weather object getting an apikey as Input
    and either a city name or lat and lon cooedinates.

    Package and example

    # Create a weather object using a city name
    # The api key below is not guaranteed to work
    # Get your own apikey from http://openweathermap.org
    # And wait a couple of hours for the api key to be activated

    >>> weather1 = Weather(apikey = "ff3481f2ba87b5929a5931deb7dde60x", city ="Madrid")

    # Using lattitude and longitude coordinates
    >>> weather2 = Weather(apikey = "ff3481f2ba87b5929a5931deb7dde60x", lat=41.1, lon =4.1)

    # Get compete weather data for the next 12 hours
    >>> weather1.next_12h()

    # Simplified data for the next 12 hours
    >>> weather1.next_12h_simplified()

    """

    def __init__(self, apikey, city=None, lat=None, lon=None):
        if city:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=imperial"
            r = requests.get(url)
            self.data = r.json()
        elif lat and lon:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}&units=imperial"
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError("Provide either a city or lat/lon arguments")

        if self.data["cod"] !="200":
            raise ValueError(self.data["message"])

    def next_12h(self):
        """
        Returns 3-hour data for the next 12 hours as a dict
        """
        return self.data['list'][:4]

    def next_12h_simplified(self):
        """Return date, temperature, and sky condition every 3 hours
           for the next 12 hours as a tupple of tuples
        """
        simple_data=[]
        for dicty in self.data['list'][:4]:
            simple_data.append((dicty['dt_txt'], dicty['main']['temp'], dicty['weather'][0]['description']))
        return simple_data


myKey = 'ff3481f2ba87b5929a5931deb7dde60f'
