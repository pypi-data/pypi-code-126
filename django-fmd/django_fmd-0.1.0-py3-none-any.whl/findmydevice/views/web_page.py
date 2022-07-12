import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.static import serve

from findmydevice import WEB_PATH


logger = logging.getLogger(__name__)


class FmdWebPageView(LoginRequiredMixin, View):
    def get(self, request):
        logger.debug('Serve FMD index.html')
        return serve(request, path='/index.html', document_root=WEB_PATH, show_indexes=False)
