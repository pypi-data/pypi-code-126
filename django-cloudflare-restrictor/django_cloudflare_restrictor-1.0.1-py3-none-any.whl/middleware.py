import re
import ipaddress
import logging

from django.core.exceptions import PermissionDenied
from django.conf import settings

from .cloudflare_ips import CLOUDFLARE_IPS_IPV4, CLOUDFLARE_IPS_IPV6

logger = logging.getLogger("django_cloudflare_restrictor")


class CloudflareRestrictorMiddleware():
    """ Middleware to restrict access, only allowing those which come via cloudflare
    """

    logger = logging.getLogger(__name__)

    def __init__(self, get_response=None):
        self.get_response = get_response

        self.enabled = getattr(settings, 'CLOUDFLARE_RESTRICTOR_ENABLED', False)
        if self.enabled:

            logger.info("Restricting inbound connections to those originating from cloudflare")

            additional_networks = getattr(settings, 'CLOUDFLARE_RESTRICTOR_ADDITIONAL_NETWORKS', [])

            self.networks = []
            for network in CLOUDFLARE_IPS_IPV4 + CLOUDFLARE_IPS_IPV6 + additional_networks:
                self.networks.append(ipaddress.ip_network(network))

            self.exclude_paths = [
                re.compile(path_re)
                for path_re in getattr(settings, 'CLOUDFLARE_RESTRICTOR_EXCLUDE_PATHS', [])
            ]

        else:

            logger.info("Cloudflare restrictions disabled")

    def __call__(self, request):

        if not self.enabled:
            return self.get_response(request)

        ip = ipaddress.ip_address(request.META.get('REMOTE_ADDR'))

        # Check to see if source IP address is in the cloudflare source IP
        # network list
        for network in self.networks:
            if ip in network:
                return self.get_response(request)

        # Check to see if the target path is in the exclude list
        for path_re in self.exclude_paths:
            if path_re.match(request.META.get('PATH')):
                return self.get_response(request)

        raise PermissionDenied()

