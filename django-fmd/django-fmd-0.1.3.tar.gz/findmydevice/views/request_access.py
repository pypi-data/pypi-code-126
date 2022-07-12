import logging
from uuid import UUID

from django.http import HttpResponseBadRequest, HttpResponseForbidden, JsonResponse
from django.views import View

from findmydevice.json_utils import parse_json
from findmydevice.models import Device
from findmydevice.models.device import new_access_token


logger = logging.getLogger(__name__)


class RequestAccessView(View):
    """
    /requestAccess
    """

    def put(self, request):  # TODO: Add lock here!
        """
        Response access token.
        """
        access_data = parse_json(request)

        hashed_password = access_data.get('HashedPassword') or access_data.get('Data')
        if not hashed_password:
            logger.error('No hashed password from "HashedPassword" or "Data" !')
            return HttpResponseBadRequest()

        # App sends hex digest in uppercase, the web page in lower case ;)
        hashed_password = hashed_password.lower()

        device_id = access_data.get('DeviceId') or access_data.get('IDT')
        if not device_id:
            logger.error('No "DeviceId" or "IDT" !')
            return HttpResponseBadRequest()

        try:
            device_id = UUID(device_id)
        except ValueError as err:
            logger.error('IDT %r is no UUID: %s', device_id, err)
            return HttpResponseForbidden()

        device = Device.objects.filter(uuid=device_id).first()
        if not device:
            logger.error('Device entry not found for: %r', device_id)
            return HttpResponseBadRequest()

        if hashed_password != device.hashed_password:
            logger.error(
                'Wrong password %r is not %r for %s',
                hashed_password,
                device.hashed_password,
                device,
            )
            return HttpResponseForbidden()

        access_token = new_access_token(device=device)
        accesstoken_reply = {'IDT': device.uuid, 'Data': access_token}
        return JsonResponse(accesstoken_reply)
