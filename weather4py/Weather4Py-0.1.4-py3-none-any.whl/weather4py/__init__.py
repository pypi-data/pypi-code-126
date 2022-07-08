__version__ = '0.1.0'
import requests, json

class WeatherMan():
    region:         str = None
    time:           str = None
    weather:        str = None
    humidity:       str = None
    temperature:    int = None
    __measurement:  str = "c"
    __url:          str = "https://weatherdbi.herokuapp.com/data/weather/"

    def __init__(self, search: str):
        self.search = search
        self.obtain_information()

    def set_measurement(self, measure_type: str):
        if (measure_type.lower() == "metric"):
            self.__measurement = "c"
        else:
            self.__measurement = "f"

    def obtain_information(self):
        r = requests.get(self.__url + self.search)
        self.__update_variables(r.json())

    def save_to_file(self, file_name: str):
        data = {
            'region'     : self.region, 
            'time'       : self.time,
            'weather'    : self.weather,
            'temperature': self.temperature,
            'humidity'   : self.humidity
        }

        with open(file_name, 'w') as output:
            json.dump(data, output)

    def __update_variables(self, json: dict):
        if ("status" in json):
            self.region         = None
            self.time           = None
            self.weather        = None
            self.humidity       = None
            self.temperature    = None
        else:   
            self.region         = json["region"]
            self.time           = json["currentConditions"]["dayhour"]
            self.weather        = json["currentConditions"]["comment"]
            self.temperature    = json["currentConditions"]["temp"][self.__measurement]
            self.humidity       = json["currentConditions"]["humidity"]



