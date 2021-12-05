"""
This module defines the test cases for department service
"""
# standard library imports

# local imports
from hospital_app import  database
from hospital_app.models.admin import Admin
from hospital_app.service import admin
from hospital_app.tests.ConfigurationTests import ConfigurationTest


class TestAdminService(ConfigurationTest):
    """
    This is the class for admin service test cases
    """

    def test_get_all_admins(self):
        """
        Adds  test records and tests the result
        """
        admin1 = Admin(username="12345", password="admin")
        admin2 = Admin(username="admin", password="12345")
        database.session.add(admin1)
        database.session.add(admin2)
        database.session.commit()
        self.assertEqual(2, len(admin.get_all_admin()))

    def test_get_admin_by_username(self):
        """
        Adds  test records and tests the result
        """
        admin1 = Admin(username="12345", password="admin")
        admin2 = Admin(username="admin", password="12345")
        database.session.add(admin1)
        database.session.add(admin2)
        database.session.commit()
        self.assertEqual(1, len([admin.get_admin_by_name('admin')]))
