from django.http import JsonResponse
from django.views import View

from findmydevice.json_utils import parse_json
from findmydevice.models import Location
from findmydevice.models.device import get_device_by_token


class LocationView(View):
    """
    /location
    """

    def post(self, request):
        location_data = parse_json(request)

        bat = location_data['bat']
        raw_date = int(location_data['date'])
        lat = location_data['lat']
        lon = location_data['lon']
        provider = location_data['provider']

        access_token = location_data['IDT']
        device = get_device_by_token(token=access_token)
        Location.objects.create(
            device=device,
            bat=bat,
            raw_date=raw_date,
            lat=lat,
            lon=lon,
            provider=provider,
        )
        response_data = {
            # TODO
        }
        return JsonResponse(response_data)

    def put(self, request):
        location_data = parse_json(request)
        access_token = location_data['IDT']
        # index = int(location_data['Data'])  # TODO: Use this index!

        device = get_device_by_token(token=access_token)

        queryset = Location.objects.filter(device=device).order_by('create_dt')
        # TODO: slice via index!

        location = queryset.latest()

        response_data = {
            'Provider': location.provider,
            'Date': location.raw_date,
            'lon': location.lon,
            'lat': location.lat,
            'Bat': location.bat,
        }
        return JsonResponse(response_data)
