from django.contrib import admin

from findmydevice.admin.fmd_admin_site import fmd_admin_site
from findmydevice.admin.mixins import NoAddPermissionsMixin
from findmydevice.models import Location


@admin.register(Location, site=fmd_admin_site)
class LocationModelAdmin(NoAddPermissionsMixin, admin.ModelAdmin):
    readonly_fields = (
        'uuid',
        'device',
        'bat',
        'raw_date',
        'lat',
        'lon',
        'provider',
        'create_dt',
        'update_dt',
    )
    list_display = ('uuid', 'create_dt', 'update_dt')
    list_filter = ('device',)
    date_hierarchy = 'create_dt'
    ordering = ('-update_dt',)

    def has_delete_permission(self, request, obj=None):
        """
        Should be always deleted via device deletion
        to remove all location entries for the device.
        """
        return False
