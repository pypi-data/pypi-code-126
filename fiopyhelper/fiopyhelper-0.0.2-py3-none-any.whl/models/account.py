import json

from fiopy.config import Config
from fiopy.enums import UserRole
from fiopy.models.base import BaseModel
from fiopy.models.plan import PlanModel
from fiopy.models.subscription import SubscriptionModel
from fiopy.models.team import TeamModel
from fiopy.http.http_request import HttpRequest
from fiopy.annotations.autowire import autowire

__all__ = ["AccountModel"]


class AccountModel(BaseModel):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.owner_id = kwargs.get("owner_id")

        self._member_count = kwargs.get("member_count")
        self._user_count = kwargs.get("user_count")
        self._collaborator_count = kwargs.get("collaborator_count")
        self._team_count = kwargs.get("team_count")
        self._project_count = kwargs.get("project_count")
        self._folder_count = kwargs.get("folder_count")
        self._file_count = kwargs.get("file_count")
        self._storage = kwargs.get("storage")
        plan = kwargs.get("plan", {})
        while isinstance(plan, str):
            plan = json.loads(plan)
        self._plan = PlanModel(**plan)
        self._duration = kwargs.get("duration")
        self._invoice_emails = kwargs.get("invoice_emails")
        self._locked_at = kwargs.get("locked_at")
        self._lifetime_file_count = kwargs.get("lifetime_file_count")

        subscription = kwargs.get("subscription", {})
        while isinstance(subscription, str):
            subscription = json.loads(subscription)
        self._subscription = SubscriptionModel(**subscription)
        self._delinquent_at = kwargs.get("delinquent_at")
        self._unpaid_at = kwargs.get("unpaid_at")
        self._company_name = kwargs.get("company_name")
        self._company_address = kwargs.get("company_address")
        self._city = kwargs.get("city")
        self._state = kwargs.get("state")
        self._postal_code = kwargs.get("postal_code")
        self._deleted_at = kwargs.get("deleted_at")
        self._vat = kwargs.get("vat")

        self._image = kwargs.get("image")
        self._archived_storage = kwargs.get("archived_storage")

        super().cleanup_values()

    @property
    def member_count(self):
        return self._member_count

    @property
    def collaborator_count(self):
        return self._collaborator_count

    @property
    def team_count(self):
        return self._team_count

    @property
    def project_count(self):
        return self._project_count

    @property
    def folder_count(self):
        return self._folder_count

    @property
    def file_count(self):
        return self._file_count

    @property
    def storage(self):
        return self._storage

    @property
    def plan(self):
        return self._plan

    @property
    def duration(self):
        return self._duration

    @property
    def invoice_emails(self):
        return self._invoice_emails

    @property
    def locked_at(self):
        return self._locked_at

    @property
    def lifetime_file_count(self):
        return self._lifetime_file_count

    @property
    def subscription(self):
        return self._subscription

    @property
    def delinquent_at(self):
        return self._delinquent_at

    @property
    def unpaid_at(self):
        return self._unpaid_at

    @property
    def company_name(self):
        return self._company_name

    @property
    def company_address(self):
        return self._company_address

    @property
    def city(self):
        return self._city

    @property
    def state(self):
        return self._state

    @property
    def postal_code(self):
        return self._postal_code

    @property
    def deleted_at(self):
        return self._deleted_at

    @property
    def vat(self):
        return self._vat

    @property
    def image(self):
        return self._image

    @property
    def archived_storage(self):
        return self._archived_storage

    @autowire(argmap={"account_id": "id"})
    def add_users_to_teams(
        self, *, account_id=None, role=UserRole.MEMBER, message=None, team_ids=None, user_emails=None, user=None
    ):
        request = (
            HttpRequest.request(Config.api["v1"]["hostname"])
            .post(Config.api["v1"]["endpoints"]["add_users_to_teams"])
            .add_path_param("account_id", account_id)
            .set_header("Authorization", user.session_id)
            .add_body_param("role", role.value)
            .add_body_param("message", message)
        )
        print("adding user to teams in account.py")
       

        if not isinstance(team_ids, list):
            team_ids = [team_ids]
        for idx, team_id in enumerate(team_ids):
            request.add_body_param(f"teams[{idx}][id]", team_id)

        if not isinstance(user_emails, list):
            user_emails = [user_emails]
        for idx, user_email in enumerate(user_emails):
            request.add_body_param(f"users[{idx}][email]", user_email)

        response = request.send()
        print(response.body)
        return response.body().value(key="success").is_equal_to(True)

    @autowire(argmap={"account_id": "id"})
    def remove_users_from_team(self, *, account_id=None, team_id=None, user_ids=None, user=None):
        request = (
            HttpRequest.request(Config.api["v1"]["hostname"])
            .post(Config.api["v1"]["endpoints"]["remove_users_from_team"])
            .add_path_param("account_id", account_id)
            .set_header("Authorization", user.session_id)
            .add_body_param(f"team[id]", team_id)
        )

        if not isinstance(user_ids, list):
            user_ids = [user_ids]
        for idx, user_id in enumerate(user_ids):
            request.add_body_param(f"users[{idx}][id]", user_id)

        response = request.send()
        return response.body().value(key="success").is_equal_to(True)

    @autowire(argmap={"account_id": "id"})
    def remove_users_from_account(self, *, account_id=None, user_ids=None, user=None):
        request = (
            HttpRequest.request(Config.api["v1"]["hostname"])
            .post(Config.api["v1"]["endpoints"]["remove_users_from_account"])
            .add_path_param("account_id", account_id)
            .set_header("Authorization", user.session_id)
        )

        if not isinstance(user_ids, list):
            user_ids = [user_ids]
        request.add_body_param(f"user_ids[]", user_ids)

        response = request.send()
        return response.body().value(key="success").is_equal_to(True)

    @autowire(argmap={"account_id": "id"})
    def update_users_role(self, *, account_id=None, role=UserRole.MEMBER, user_ids=None, user=None):
        request = (
            HttpRequest.request(Config.api["v1"]["hostname"])
            .post(Config.api["v1"]["endpoints"]["update_users_role"])
            .add_path_param("account_id", account_id)
            .set_header("Authorization", user.session_id)
            .add_body_param("role", role.value)
        )

        if not isinstance(user_ids, list):
            user_ids = [user_ids]
        for idx, user_id in enumerate(user_ids):
            request.add_body_param(f"users[{idx}][id]", user_id)

        response = request.send()
        return response.body().value(key="success").is_equal_to(True)

    @autowire(argmap={"account_id": "id"})
    def add_team_manager(self, *, account_id=None, team_id=None, user_id=None, user=None):
        response = (
            HttpRequest.request(Config.api["v1"]["hostname"])
            .post(Config.api["v1"]["endpoints"]["add_team_manager"])
            .add_path_param("account_id", account_id)
            .set_header("Authorization", user.session_id)
            .add_body_param(f"team[id]", team_id)
            .add_body_param(f"user[id]", user_id)
            .send()
        )

        return response.body().value(key="success").is_equal_to(True)

    @autowire(argmap={"account_id": "id"})
    def remove_team_manager(self, *, account_id=None, team_id=None, user_id=None, user=None):
        response = (
            HttpRequest.request(Config.api["v1"]["hostname"])
            .post(Config.api["v1"]["endpoints"]["remove_team_manager"])
            .add_path_param("account_id", account_id)
            .set_header("Authorization", user.session_id)
            .add_body_param(f"team[id]", team_id)
            .add_body_param(f"user[id]", user_id)
            .send()
        )

        return response.body().value(key="success").is_equal_to(True)

    @autowire(argmap={"account_id": "id"})
    def get_teams(self, *, account_id=None, user=None):
        response = (
            HttpRequest.request(Config.api["v1"]["hostname"])
            .get(Config.api["v1"]["endpoints"]["get_account_teams"])
            .add_path_param("account_id", account_id)
            .set_header("Authorization", user.session_id)
            .send()
        )
        print(vars(response))
        return response.to_models(model_clazz=TeamModel, key="teams")
