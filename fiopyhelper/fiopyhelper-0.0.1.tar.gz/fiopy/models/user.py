from fiopy.config import Config
from fiopy.enums import SessionMethod, UserRole
from fiopy.models.account import AccountModel
from fiopy.models.base import BaseModel
from fiopy.models.team import TeamModel
from fiopy.models.project import ProjectModel
from fiopy.http.http_request import HttpRequest
from fiopy.annotations.autowire import autowire


class UserModel(BaseModel):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self._email = kwargs.get("email")
        self._password = kwargs.get("password")
        self._organization = kwargs.get("organization")
        try:
            self._role = UserRole(kwargs.get("role"))
        except ValueError:
            self._role = None
        self._account_id = kwargs.get("account_id")
        self._session_jwt = kwargs.get("session_jwt")
        self._session_pat = kwargs.get("session_pat")
        self._session_id = self._session_jwt if self._session_jwt else self._session_pat
        self._session_method = SessionMethod.JWT if self._session_jwt else SessionMethod.PAT
        self._bio = None
        self._deleted_at = None
        self._digest_frequency = None
        self._email_confirm_by = None
        self._email_preferences = None
        self._features_seen = None
        self._first_login_at = None
        self._from_google = None
        self._image_128 = None
        self._image_256 = None
        self._image_32 = None
        self._image_64 = None
        self._inserted_at = None
        self._joined_via = None
        self._last_seen = None
        self._location = None
        self._name = None
        self._next_digest_date = None
        self._phone = None
        self._profile_image = None
        self._profile_image_original = None
        self._roles = None
        self._timezone_value = None
        self._updated_at = None
        self._upload_url = None
        self._user_default_color = None
        self._user_hash = None

        self.get_me()

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @property
    def organization(self):
        return self._organization

    @organization.setter
    def organization(self, org):
        self.organization = org

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, ro):
        self._role = UserRole(ro)

    @property
    def account_id(self):
        return self._account_id

    @property
    def session_jwt(self):
        return self._session_jwt

    @property
    def session_pat(self):
        return self._session_pat

    @property
    def session_id(self):
        return self._session_id

    @property
    def session_method(self):
        return self._session_method

    @session_method.setter
    def session_method(self, method):
        self._session_id = getattr(self, method.value)
        self._session_method = method

    @property
    def from_google(self):
        return self._from_google

    @property
    def image_128(self):
        return self._image_128

    @property
    def image_256(self):
        return self._image_256

    @property
    def image_32(self):
        return self._image_32

    @property
    def image_64(self):
        return self._image_64

    @property
    def inserted_at(self):
        return self._inserted_at

    @property
    def joined_via(self):
        return self._joined_via

    @property
    def last_seen(self):
        return self._last_seen

    @property
    def location(self):
        return self._location

    @property
    def name(self):
        return self._name

    @property
    def next_digest_date(self):
        return self._next_digest_date

    @property
    def phone(self):
        return self._phone

    @property
    def profile_image(self):
        return self._profile_image

    @property
    def profile_image_original(self):
        return self._profile_image_original

    @property
    def roles(self):
        return self._roles

    @property
    def timezone_value(self):
        return self._timezone_value

    @property
    def updated_at(self):
        return self._updated_at

    @property
    def upload_url(self):
        return self._upload_url

    @property
    def user_default_color(self):
        return self._user_default_color

    @property
    def user_hash(self):
        return self._user_hash

    def get_me(self):
        response = (
            HttpRequest.request(Config.api["v2"]["hostname"])
            .get(Config.api["v2"]["endpoints"]["get_me"])
            .set_header("Authorization", self.session_id)
            .send()
        )

        body = response.body().get()
        print(body)
        self._id = body["id"]
        self._account_id = body["account_id"]
        self._bio = body["bio"]
        self._deleted_at = body["deleted_at"]
        self._digest_frequency = body["digest_frequency"]
        self._email_confirm_by = body["email_confirm_by"]
        self._email_preferences = body["email_preferences"]
        self._features_seen = body["features_seen"]
        self._first_login_at = body["first_login_at"]
        self._from_google = body["from_google"]
        self._image_128 = body["image_128"]
        self._image_256 = body["image_256"]
        self._image_32 = body["image_32"]
        self._image_64 = body["image_64"]
        self._inserted_at = body["inserted_at"]
        self._joined_via = body["joined_via"]
        self._last_seen = body["last_seen"]
        self._location = body["location"]
        self._name = body["name"]
        self._next_digest_date = body["next_digest_date"]
        self._phone = body["phone"]
        self._profile_image = body["profile_image"]
        self._profile_image_original = body["profile_image_original"]
        self._roles = body["roles"]
        self._timezone_value = body["timezone_value"]
        self._updated_at = body["updated_at"]
        self._upload_url = body["upload_url"]
        self._user_default_color = body["user_default_color"]
        self._user_hash = body["user_hash"]

        super().cleanup_values()

        return self

    @autowire()
    def get_accounts(self, *, user=None):
        response = (
            HttpRequest.request(Config.api["v2"]["hostname"])
            .get(Config.api["v2"]["endpoints"]["get_accounts"])
            .set_header("Authorization", user.session_id)
            .send()
        )

        return response.to_models(model_clazz=AccountModel)

    @autowire(argmap={"account_id": "account_id"})
    def get_account(self, *, account_id=None, user=None):
        response = (
            HttpRequest.request(Config.api["v2"]["hostname"])
            .get(Config.api["v2"]["endpoints"]["get_account"])
            .add_path_param("account_id", account_id)
            .set_header("Authorization", user.session_id)
            .send()
        )

        return response.to_model(model_clazz=AccountModel)

    @autowire(argmap={"user_id": "id"})
    def get_teams(self, *, user_id, user=None):
        response = (
            HttpRequest.request(Config.api["v1"]["hostname"])
            .get(Config.api["v1"]["endpoints"]["get_user_teams"])
            .add_path_param("user_id", user_id)
            .set_header("Authorization", user.session_id)
            .send()
        )
        print(response.body.get())
        return response.to_models(model_clazz=TeamModel, key="teams")

    @autowire()
    def get_team(self, *, team_id=None, user=None):
        response = (
            HttpRequest.request(Config.api["v1"]["hostname"])
            .get(Config.api["v1"]["endpoints"]["get_team"])
            .add_path_param("team_id", team_id)
            .set_header("Authorization", user.session_id)
            .send()
        )

        return response.to_model(model_clazz=TeamModel)

    @autowire()
    def get_project(self, *, project_id=None, user=None):
        response = (
            HttpRequest.request(Config.api["v1"]["hostname"])
            .get(Config.api["v2"]["endpoints"]["get_project"])
            .add_path_param("project_id", project_id)
            .set_header("Authorization", user.session_id)
            .send()
        )

        return response.to_model(model_clazz=ProjectModel)
