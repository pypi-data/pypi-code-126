from uuid import UUID

from django.test import TestCase
from model_bakery import baker

from findmydevice.models import Device


class DeviceModelTests(TestCase):
    def test_str_repr(self):
        device = baker.make(Device, uuid=UUID(int=1), name=None)
        device.full_clean()
        assert str(device) == '>no name< (00000000-0000-0000-0000-000000000001)'
        assert repr(device) == '<Device: >no name< (00000000-0000-0000-0000-000000000001)>'

        device.name = 'Smartphone John'
        device.full_clean()
        assert str(device) == 'Smartphone John'
        assert repr(device) == '<Device: Smartphone John>'
