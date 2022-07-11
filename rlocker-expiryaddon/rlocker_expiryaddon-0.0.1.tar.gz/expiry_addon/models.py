from django.db import models
from lockable_resource.models import LockableResource
from datetime import timedelta


class ResourceExpiryPolicy(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    lockable_resource = models.OneToOneField(LockableResource, on_delete=models.PROTECT)
    expiry_hour = models.IntegerField(default=0)


    @property
    def expiry_date(self):
        if self.lockable_resource.is_locked:
            final_expiry_date = self.lockable_resource.locked_time
            final_expiry_date += timedelta(hours=self.expiry_hour)
            return final_expiry_date

    @property
    def is_expired(self):
        if self.lockable_resource.is_locked:
            return self.expiry_date < self.lockable_resource.locked_time

    def __str__(self):
        return f"{self.name}"

    # Meta Class
    class Meta:
        # Override verbose name plural to get nicer description in Admin Page:
        verbose_name_plural = "Resource Expiry Policies"