"""
This module defines the test cases for department views
"""

# local imports
from hospital_app import database
from hospital_app.models.hospital import Hospital
from hospital_app.tests.ConfigurationTests import ConfigurationTest


class TestDepartmentOfHospitalViews(ConfigurationTest):
    """
    This is the class for department of hospital views test cases
    """

    def test_homepage(self):
        """
        Tests whether the get request on homepage page works correctly,
        returning the status code 200
        """
        response = self.app.get('/')
        self.assertEqual(200, response.status_code)

    def test_departments_of_hospital(self):
        """
        Tests whether the get request on departments page works correctly,
        returning the status code 200
        """
        response = self.app.get('/hospitals')
        self.assertEqual(200, response.status_code)

    def test_add_departments_of_hospital(self):
        """
        Tests whether the get request on add department page works correctly,
        returning the status code 200
        """
        response = self.app.get('/hospital/add')
        self.assertEqual(200, response.status_code)

    def test_department_of_hospital_added(self):
        """
        Tests whether the get request on add department page works correctly,
        and redirects to departments page, returning the status code 302
        """
        response = self.app.get('/hospital/add?added=true')
        self.assertEqual(302, response.status_code)

    def test_department_of_hospital_not_added(self):
        """
        Tests whether the get request on add department page works correctly,
        and redirects to department page, returning the status code 302
        """
        response = self.app.get('/hospital/add?added=false')
        self.assertEqual(302, response.status_code)

    def test_edit_department(self):
        """
        Tests whether the get request on edit department page works correctly,
        returning the status code 200
        """
        department = Hospital(name="first hospital", to_do="something do")
        database.session.add(department)
        database.session.commit()
        response = self.app.get('/hospital/edit/1')
        self.assertEqual(200, response.status_code)

    def test_department_of_hospital_edited(self):
        """
        Tests whether the get request on edit department page works correctly,
        and redirects to departments page, returning the status code 302
        """
        department = Hospital(name="department1", to_do="to_do")
        database.session.add(department)
        database.session.commit()
        response = self.app.get('/hospital/edit/1?edited=true')
        self.assertEqual(302, response.status_code)

    def test_department_not_edited(self):
        """
        Tests whether the get request on edit department page works correctly,
        and redirects to department page, returning the status code 302
        """
        department = Hospital(name="department2", to_do="description1")
        database.session.add(department)
        database.session.commit()
        response = self.app.get('/hospital/edit/1?edited=false')
        self.assertEqual(302, response.status_code)

    def test_delete_department(self):
        """
        Tests whether the get request on delete department page works correctly,
        returning the status code 200
        """
        department = Hospital(name="first hospital8", to_do="2")
        database.session.add(department)
        database.session.commit()
        response = self.app.get('/hospital/delete/1')
        self.assertEqual(302, response.status_code)
