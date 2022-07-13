
from django.contrib import admin

from tecdoc.models import Supplier, Article


admin.site.register(
    Supplier,
    list_display=['description', 'matchcode'],
    search_fields=['description', 'matchcode']
)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ['article_number', 'description', 'supplier']
    search_fields = ['clean_article_number']
    list_filter = ['supplier']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.GET.get('supplier__id__exact'):
            return queryset.none()
        return queryset
