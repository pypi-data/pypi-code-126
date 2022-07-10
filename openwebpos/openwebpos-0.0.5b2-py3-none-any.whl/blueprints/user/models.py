from collections import OrderedDict

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from openwebpos.extensions import db
from openwebpos.utils.sql import SQLMixin


class User(UserMixin, SQLMixin, db.Model):
    __tablename__ = "user"
    ROLE = OrderedDict([
        ('customer', 'Customer'),
        ('staff', 'Staff'),
        ('admin', 'Admin')
    ])
    # Authentication
    role = db.Column(db.Enum(*ROLE, name='role_types', native_enum=False), index=True, nullable=False,
                     server_default='customer')
    username = db.Column(db.String(120), unique=True, index=True)
    email = db.Column(db.String(128), unique=True, index=True)
    password = db.Column(db.String(120), nullable=False, server_default='')
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

    def check_password(self, password):
        return check_password_hash(password, self.password)

    def is_active(self):
        """
        Return whether user account is active.
        :return: bool
        """
        return self.active

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
