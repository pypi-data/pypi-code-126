import os
import ipaddress
import logging

from django.core.exceptions import PermissionDenied
from django.conf import settings

from .cloudflare_ips import CLOUDFLARE_IPS_IPV4, CLOUDFLARE_IPS_IPV6


class CloudflareRestrictorMiddleware():
    """ Middleware to restrict access, only allowing those which come via cloudflare
    """

    logger = logging.getLogger(__name__)

    def __init__(self, get_response=None):
        self.get_response = get_response

        self.enabled = getattr(settings, 'CLOUDFLARE_RESTRICTOR_ENABLED', False)
        if self.enabled:

            additional_networks = getattr(settings, 'CLOUDFLARE_RESTRICTOR_ADDITIONAL_NETWORKS', [])

            self.networks = []
            for network in CLOUDFLARE_IPS_IPV4 + CLOUDFLARE_IPS_IPV6 + additional_networks:
                self.networks.append(ipaddress.ip_network(network))

        self.enabled = getattr(settings, 'ENFORCE_CLOUDFLARE', False)

    def __call__(self, request):
        if self.enabled:
            ip = ipaddress.ip_address(request.META.get('REMOTE_ADDR'))

            matched = False

            for network in self.networks:
                if ip in network:
                    matched = True
                    break

            if matched:
                response = self.get_response(request)
                return response
            else:
                raise PermissionDenied()

        response = self.get_response(request)
        return response

