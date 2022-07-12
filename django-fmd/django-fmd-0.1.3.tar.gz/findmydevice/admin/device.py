from django.contrib import admin
from django.db.models import Count
from django.utils.translation import gettext_lazy as _

from findmydevice.admin.fmd_admin_site import fmd_admin_site
from findmydevice.admin.mixins import NoAddPermissionsMixin
from findmydevice.models import Device


@admin.register(Device, site=fmd_admin_site)
class DeviceModelAdmin(NoAddPermissionsMixin, admin.ModelAdmin):
    readonly_fields = ('uuid', 'hashed_password', 'privkey', 'pubkey', 'create_dt', 'update_dt')
    list_display = (
        'uuid',
        'name',
        'location_count',
        'last_location_date',
        'create_dt',
        'update_dt',
    )
    list_filter = ('name',)
    date_hierarchy = 'create_dt'
    ordering = ('-update_dt',)

    @admin.display(description=_('Last Location'))
    def last_location_date(self, obj):
        return obj.location_set.latest().create_dt

    @admin.display(description=_('Location count'))
    def location_count(self, obj):
        return obj.location_count

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(
            location_count=Count('location', distinct=True),
        )
        return qs
