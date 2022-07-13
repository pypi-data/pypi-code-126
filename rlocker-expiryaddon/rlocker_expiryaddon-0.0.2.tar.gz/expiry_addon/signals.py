from django.db.models.signals import post_save
from django.dispatch import receiver
from expiry_addon.models import ResourceExpiryPolicy


@receiver(post_save, sender=ResourceExpiryPolicy)
def generate_field_values_if_empty(sender, instance, created, **kwargs):
    """
    For some fields we'd like to generate values if they left empty.
    Using blank=true and null=true is effective, but the default value we'd
        like to generate, is based on another IntegerField which is required
    For Example:
    ResourceExpiryPolicy(
        name="",
        expiry_hour=24,
        lockable_resource=1TO1Field('some_resource_1')
    )
    We'd like to have this after post_save():
        ResourceExpiryPolicy(
        name="H24-some-resource-1",
        expiry_hour=24,
        lockable_resource=1TO1Field('some_resource_1')
    )
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return: None
    """
    if created:
        if not instance.name:
            instance.name = f"H{instance.expiry_hour}-{instance.lockable_resource.name}"
            instance.save()

    if not created:
        pass