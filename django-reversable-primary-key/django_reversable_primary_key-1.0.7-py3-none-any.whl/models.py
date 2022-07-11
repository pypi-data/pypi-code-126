from python_utils.time_utils import convert_from_utc_epoch
from reversable_primary_key.primary_key import reverse_id


class CreatedModelMixin():

    @property
    def created(self):
        try:
            return  convert_from_utc_epoch(reverse_id(self.id))
        except Exception:
            return None