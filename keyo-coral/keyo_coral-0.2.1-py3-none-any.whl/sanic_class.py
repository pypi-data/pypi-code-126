from sanic.views import HTTPMethodView
from sanic.response import json
from sanic.log import logger
from sdk_functions import change_led, buzzer_beep, get_media


class ChangeLedRoutes(HTTPMethodView):
    """class function for change led"""

    async def get(self, request):
        """filtering data on based created_at"""
        change_led()
        logger.info("change_led is successfully done")

        return json(
            {
                "status": "success",
                "message": "Led change"
            }
        )


class BuzzerBeepRoutes(HTTPMethodView):
    """class function for buzzer_beep"""

    async def get(self, request):
        """filtering data on based created_at"""
        buzzer_beep()
        logger.info("buzzer_beep is successfully done")

        return json(
            {
                "status": "success",
                "message": "buzzer_beep"
            }
        )


class GetMediaRoutes(HTTPMethodView):
    """class function for change led"""

    async def get(self, request):
        """filtering data on based created_at"""
        get_media()
        logger.info("get_media is successfully done")

        return json(
            {
                "status": "success",
                "message": "get_media"
            }
        )
