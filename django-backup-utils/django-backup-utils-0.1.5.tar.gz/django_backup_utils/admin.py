import os
from pathlib import Path

from django.contrib import admin
from django_backup_utils import models
from django.utils.safestring import mark_safe
from django.urls import reverse_lazy
from django.contrib import messages


class BackupLogAdmin(admin.ModelAdmin):
    list_filter = ("module",)
    list_display = (
        "pk", "module", "message", "backup", "size_mb", "success", "executed_at",)
    readonly_fields = ("module", "message", "backup", "size_bytes", "success", "executed_at", "params", "output",)

    def has_add_permission(self, request, obj=None):
        return False

    def restore_link(self, obj):
        if obj.module == "createbackup":
            return mark_safe(f'<a href="{reverse_lazy("restore-backup", kwargs={"pk": obj.pk})}">restore</a>')

    def size_mb(self, obj):
        if obj.size_bytes:
            return f"{round(float(obj.size_bytes / 1000 / 1000), 2)} MB"
        return ""


class BackupAdmin(admin.ModelAdmin):
    list_display = (
        "pk", "backup", "size_mb", "created_at", "restore_link",
        "system_migrations_migrated",
        "system_migration_files", "dump_version", "system_version",)
    readonly_fields = ("backup", 'size_bytes', "created_at", "system_migrations_migrated",
                       "system_migration_files", "dump_version", "system_version", "params",)
    list_display_links = ("pk", "restore_link",)

    change_list_template = "django_backup_utils/backup_changelist.html"

    def has_add_permission(self, request, obj=None):
        return False

    def restore_link(self, obj):
        return mark_safe(f'<a href="{reverse_lazy("restore-backup", kwargs={"pk": obj.pk})}">restore</a>')

    def size_mb(self, obj):
        if obj.size_bytes:
            return f"{round(float(obj.size_bytes / 1000 / 1000), 2)} MB"
        return ""

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            backup = Path(obj.backup)
            if backup.is_file():
                os.remove(backup)
                models.BackupLog.objects.create(message="deleted backup", module="admin:backup_delete",
                                                output=f"deleted {backup}",
                                                backup=obj.backup,
                                                size_bytes=obj.size_bytes,
                                                success=True)
                messages.success(request, f'deleted {obj.backup}')
            else:
                models.BackupLog.objects.create(message="deleted backup object", module="admin:backup_delete",
                                                output=f"backup file was not found",
                                                backup=obj.backup, )
                messages.info(request, f'deleted only object {obj}; ({obj.backup} was not found)')
            obj.delete()


admin.site.register(models.Backup, BackupAdmin)
admin.site.register(models.BackupLog, BackupLogAdmin)
