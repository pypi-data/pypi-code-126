from sanic import Sanic
from sanic_class import ChangeLedRoutes, BuzzerBeepRoutes, GetMediaRoutes
import logging

app = Sanic(__name__)

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "logfile.log",
                    filemode = "w",
                    format = Log_Format,
                    level = logging.ERROR)


app.add_route(ChangeLedRoutes.as_view(), "/change_led")
app.add_route(BuzzerBeepRoutes.as_view(), "/buzzer_beep")
app.add_route(GetMediaRoutes.as_view(), "/get_media")



if __name__ == "__main__":
    app.run(port=2000, workers=1)