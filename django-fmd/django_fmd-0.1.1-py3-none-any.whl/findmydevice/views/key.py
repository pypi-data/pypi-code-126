from django.http import HttpResponse
from django.views import View

from findmydevice.json_utils import parse_json
from findmydevice.models import Device
from findmydevice.models.device import get_device_by_token


class KeyView(View):
    """
    /key
    """

    def put(self, request):
        """
        e.g:
            {'Data': '1', 'IDT': 'LPYzPAFwLa8u'}
        """
        put_data = parse_json(request)
        access_token = put_data['IDT']
        # index = int(put_data['Data'])  # TODO: Use this index!

        device: Device = get_device_by_token(token=access_token)
        privkey = device.privkey
        return HttpResponse(content_type='application/text', content=privkey)
