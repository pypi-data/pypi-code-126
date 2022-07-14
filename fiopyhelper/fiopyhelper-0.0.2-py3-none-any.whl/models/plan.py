import json
from fiopy.models.base import BaseModel
from fiopy.models.plan_features import PlanFeaturesModel

__all__ = ["PlanModel"]


class PlanModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._cost = kwargs.get("cost")

        self._name = kwargs.get("name")
        self._title = kwargs.get("title")
        self._payment_method = kwargs.get("payment_method")
        self._period = kwargs.get("period")
        self._enterprise = kwargs.get("enterprise")
        self._default_plan = kwargs.get("default_plan")
        self._tier = kwargs.get("tier")

        self._member_limit = kwargs.get("member_limit")
        self._collaborator_limit = kwargs.get("collaborator_limit")
        self._autoscaling = kwargs.get("autoscaling")
        self._archived_storage_limit = kwargs.get("archived_storage_limit")
        self._file_limit = kwargs.get("file_limit")
        self._lifetime_file_limit = kwargs.get("lifetime_file_limit")
        self._project_limit = kwargs.get("project_limit")
        self._storage_limit = kwargs.get("storage_limit")
        self._team_limit = kwargs.get("team_limit")

        available_features = kwargs.get("available_features", {})
        while isinstance(available_features, str):
            available_features = json.loads(available_features)
        self._available_features = PlanFeaturesModel(**available_features)

        self._updated_at = kwargs.get("updated_at")
        self._version = kwargs.get("version")

        super().cleanup_values()

    @property
    def cost(self):
        return self._cost

    @property
    def name(self):
        return self._name

    @property
    def title(self):
        return self._title

    @property
    def payment_method(self):
        return self._payment_method

    @property
    def period(self):
        return self._period

    @property
    def enterprise(self):
        return self._enterprise

    @property
    def default_plan(self):
        return self._default_plan

    @property
    def tier(self):
        return self._tier

    @property
    def member_limit(self):
        return self._member_limit

    @property
    def collaborator_limit(self):
        return self._collaborator_limit

    @property
    def autoscaling(self):
        return self._autoscaling

    @property
    def archived_storage_limit(self):
        return self._archived_storage_limit

    @property
    def file_limit(self):
        return self._file_limit

    @property
    def lifetime_file_limit(self):
        return self._lifetime_file_limit

    @property
    def project_limit(self):
        return self._project_limit

    @property
    def storage_limit(self):
        return self._storage_limit

    @property
    def team_limit(self):
        return self._team_limit

    @property
    def available_features(self):
        return self._available_features

    @property
    def updated_at(self):
        return self._updated_at

    @property
    def version(self):
        return self._version

