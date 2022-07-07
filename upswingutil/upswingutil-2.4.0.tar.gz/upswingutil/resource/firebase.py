import logging

from firebase_admin import auth, get_app
from firebase_admin.auth import UserNotFoundError


class FirebaseHelper:

    def __init__(self, appName=None):
        self.appName = appName
        self.app = get_app(self.appName)

    def find_user_by_email(self, email):
        try:
            return auth.get_user_by_email(email, app=self.app)
        except UserNotFoundError as userNotFound:
            logging.error(f'User not found in {self.appName} for given email id')
            return None

    def create_user(self):
        pass
