import json
from django.contrib import admin
from .models import Stat
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.conf import settings
# Register your models here.

@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):

    list_display = ['windows','mac','iphone','android','others','total']

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None) -> bool:
        return False
    
    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def changelist_view(self, request, extra_context=None):
        stat_data = Stat.objects.values('windows','mac','iphone',"android","others")
        json_data = json.dumps(list(stat_data),cls=DjangoJSONEncoder)
        bg_color = 'rgba(255,255,255,0.1)'
        border_color = 'rgba(0,0,255,0.2)'
        if hasattr(settings,"REQUEST_ANALYZER_BG_COLOR"):
            bg_color = 'rgba' + str(settings.REQUEST_ANALYZER_BG_COLOR)
        if hasattr(settings,"REQUEST_ANALYZER_CHART_COLOR"):
            border_color = 'rgba' + str(settings.REQUEST_ANALYZER_CHART_COLOR)
        bg_color_json_encoded = json.dumps(bg_color,cls=DjangoJSONEncoder)
        border_color_json_encoded = json.dumps(border_color,cls=DjangoJSONEncoder)
        extra_context = {
            'stat_data':json_data,
            "background_color":bg_color_json_encoded,
            'border_color':border_color_json_encoded,
            'title':'Requesting OS Statistics'
            }
        return super().changelist_view(request, extra_context)