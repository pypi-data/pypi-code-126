from django.db import models

# Create your models here.


class Stat(models.Model):
    windows = models.IntegerField(default=0)
    mac = models.IntegerField(default=0)
    android = models.IntegerField(default=0)
    iphone = models.IntegerField(default=0)
    others = models.IntegerField(default=0)

    def total(self, *args, **kwargs):
        return self.windows + self.mac + self.android + self.iphone + self.others