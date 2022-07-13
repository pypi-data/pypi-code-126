import uuid
import sys

import django
from django.contrib import admin, messages
from django.http import JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.translation import gettext_lazy as _
from django.core.cache import cache

from gift_card_crawler.utils import crawl_runner
from gift_card_crawler.models import GiftCardCrawler
from gift_card_crawler.utils import extract_links
from multiprocessing import Process


@admin.register(GiftCardCrawler)
class GiftCardCrawlerAdmin(admin.ModelAdmin):
    def get_urls(self):
        info = self.model._meta.app_label, self.model._meta.module_name
        return [
            path(r'', self.admin_site.admin_view(self.changelist_view), name='%s_%s_changelist' % info),
            path(r'cards-info/<uuid:reference_id>/', self.admin_site.admin_view(self.cards_info), name='%s_%s_cards_info' % info),
        ]

    def changelist_view(self, request, extra_context=None):
        context = dict(
            self.admin_site.each_context(request),
            django_version=django.get_version(),
            jet=('jet' in sys.modules),
        )

        if request.method == 'POST':
            reference_id = str(uuid.uuid4())
            file = request.FILES.get('gift_card_link')
            if not file:
                self.message_user(request, _('The File is required.'), level=messages.ERROR)
                return redirect('admin:gift_card_crawler_gift_cards_crawler_changelist')

            links, error = extract_links(file)
            if not links:
                self.message_user(request, error, level=messages.ERROR)
                return redirect('admin:gift_card_crawler_gift_cards_crawler_changelist')

            crawl_process = Process(target=crawl_runner, args=(links, reference_id, ))
            crawl_process.start()

            context['reference_id'] = reference_id

        return TemplateResponse(request, "gift_card_crawler/admin/change_form.html", context=context)

    def cards_info(self, request, reference_id):
        cards = cache.get(str(reference_id))
        response = {'cards_datatable': None}
        if cards:
            context = {
                'django_version': django.get_version(),
                'jet': ('jet' in sys.modules),
                'cards': cards
            }
            cards_datatable = render_to_string('gift_card_crawler/admin/cards_datatable.html', context)
            response = {'cards_datatable': cards_datatable}
        return JsonResponse(response)
