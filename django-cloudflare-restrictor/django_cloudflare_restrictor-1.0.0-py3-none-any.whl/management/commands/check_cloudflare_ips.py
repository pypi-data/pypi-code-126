import uuid
from django.core.management.base import BaseCommand, CommandError

import urllib.request

from django_cloudflare_restrictor.cloudflare_ips import CLOUDFLARE_IPS_IPV4, CLOUDFLARE_IPS_IPV6

import logging

logger = logging.getLogger("django_cloudflare_restrictor")


class Command(BaseCommand):
    help = 'Check latest IP lists from cloudflare are up to date'

    def handle(self, *args, **options):
        headers = {'User-Agent': 'Django Cloudflare Restrictor'}

        request =urllib.request.Request('https://www.cloudflare.com/ips-v4', headers=headers)
        with urllib.request.urlopen(request) as f:
            ipv4_list = f.read().decode('utf-8').split('\n')

        request =urllib.request.Request('https://www.cloudflare.com/ips-v6', headers=headers)
        with urllib.request.urlopen(request) as f:
            ipv6_list = f.read().decode('utf-8').split('\n')

        removed_ipv4 = set(CLOUDFLARE_IPS_IPV4) - set(ipv4_list)
        added_ipv4 = set(ipv4_list) - set(CLOUDFLARE_IPS_IPV4)
        removed_ipv6 = set(CLOUDFLARE_IPS_IPV6) - set(ipv6_list)
        added_ipv6 = set(ipv6_list) - set(CLOUDFLARE_IPS_IPV6)

        if removed_ipv4 or added_ipv4 or removed_ipv6 or added_ipv6:
            logger.warning("Cloudflare IP list has been updated, please upgrade the django_cloudflare_restrictor package")

        if options['debug']:
            for addr in removed_ipv4:
                logger.info(f"Removed IPv4 address: {addr}")
            for addr in added_ipv4:
                logger.info(f"Added IPv4 address: {addr}")
            for addr in removed_ipv6:
                logger.info(f"Removed IPv6 address: {addr}")
            for addr in added_ipv6:
                logger.info(f"Added IPv6 address: {addr}")

    def add_arguments(self, parser):
        parser.add_argument(
            '--debug',
            action='store_true',
            help='Show what IP addresses have changed'
        )

