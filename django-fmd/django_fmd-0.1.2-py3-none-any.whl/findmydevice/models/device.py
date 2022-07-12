import logging
import uuid

from bx_django_utils.models.timetracking import TimetrackingBaseModel
from django.conf import settings
from django.core.cache import cache
from django.db import models
from django.http import Http404
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_lazy as _


logger = logging.getLogger(__name__)


class Device(TimetrackingBaseModel):
    """
    In FMD project it's named "user"
    """

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        help_text=_('Optional Name for this Device. e.g.: Username ;) Just displayed in the admin'),
    )
    hashed_password = models.CharField(max_length=64)
    privkey = models.CharField(max_length=2048, unique=True)
    pubkey = models.CharField(max_length=512, unique=True)
    # command2user=
    # push_url=
    # location_data=
    # pictures=

    def __str__(self):
        if self.name:
            return self.name
        return f'>no name< ({self.uuid})'


def _make_cache_key(token):
    cache_key = f'access_token_{token}'
    logger.debug('Cache key: %r', cache_key)
    return cache_key


def new_access_token(device: Device):
    token = get_random_string(length=12)
    timeout = settings.FMD_ACCESS_TOKEN_TIMEOUT_SEC
    cache.set(key=_make_cache_key(token), value=device.uuid, timeout=timeout)
    logger.info('Store access token %r for %s (timeout: %i sec)', token, device.uuid, timeout)
    return token


def get_device_by_token(token):
    device_uuid = cache.get(key=_make_cache_key(token))
    if device_uuid:
        logger.debug('Token %r == %r', token, device_uuid)
        device = Device.objects.filter(uuid=device_uuid).first()
        if device:
            logger.debug('Found device %s for token %r', device, token)
            return device
        else:
            logger.error('Device not found for token: %r', token)
    else:
        logger.error('Token %r not valid or expired', token)

    raise Http404
