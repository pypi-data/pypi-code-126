from django.contrib import admin

from findmydevice.admin.fmd_admin_site import fmd_admin_site
from findmydevice.admin.mixins import NoAddPermissionsMixin
from findmydevice.models import Device


@admin.register(Device, site=fmd_admin_site)
class DeviceModelAdmin(NoAddPermissionsMixin, admin.ModelAdmin):
    readonly_fields = ('uuid', 'hashed_password', 'privkey', 'pubkey', 'create_dt', 'update_dt')
    list_display = ('uuid', 'name', 'create_dt', 'update_dt')
    list_filter = ('name',)
    date_hierarchy = 'create_dt'
    ordering = ('-update_dt',)
