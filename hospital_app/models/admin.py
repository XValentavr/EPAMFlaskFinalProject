"""
Employee model used to represent admin user, this module defines the
following classes:
- `Admin`, admin user  model
"""
from flask_login import UserMixin

from hospital_app import database


class Admin(UserMixin, database.Model):
    """
    Model representing admins
    :param str username: admin's name
    :param date password: admin's hash password

    """

    #: Name of the database table storing admin
    __tablename__ = 'admin'

    #: admin's database id
    id = database.Column(database.Integer(), primary_key=True)

    #: admin's name
    username = database.Column(database.String(length=255), nullable=False, unique=True)

    #: admin's password
    password = database.Column(database.String(length=255), nullable=False)

    def __init__(self, username, password):
        #: admin's name
        self.username = username
        #: admin's date of birth
        self.password = password
