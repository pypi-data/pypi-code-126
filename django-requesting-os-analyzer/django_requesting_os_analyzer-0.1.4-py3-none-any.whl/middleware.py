from django.db.models import F
from .models import Stat



class CounterMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response


    def stats(self, os_info):
        os_info = os_info.lower()
        if "windows" in os_info:
            Stat.objects.all().update(windows=F("windows")+1)
        elif "macintosh" in os_info:
            Stat.objects.all().update(mac=F("mac")+1)
        elif "iphone" in os_info:
            Stat.objects.all().update(iphone=F("iphone")+1)
        elif "android" in os_info:
            Stat.objects.all().update(android=F("android")+1)
        else:
            Stat.objects.all().update(others=F("others")+1)




    def __call__(self, request):

        if not Stat.objects.count():
            Stat.objects.create()


        if "admin" not in request.path:
            self.stats(request.META['HTTP_USER_AGENT'])




        response = self.get_response(request) 
        return response
        