"""
This module defines crud operations to work with admin table
"""
from hospital_app.models.admin import Admin


def get_admin_by_name(username: str):
    """
    This function is used to get the single admin by id
    :param username: the username of the admin to get
    :return: the admin  with the specified username
    """
    admin = Admin.query.filter_by(username=username).first()
    return admin if admin is not None else None


def get_all_admin() -> str:
    """
    This function is used to get the single admin by id
    :return: the admin  with the specified username
    """
    admin = Admin.query.all()
    return admin if admin is not None else None
