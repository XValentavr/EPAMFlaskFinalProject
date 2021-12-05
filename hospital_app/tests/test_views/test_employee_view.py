"""
This module defines the test cases for employee views
"""

# local imports
from datetime import datetime
from hospital_app import database
from hospital_app.models.employee import Employee
from hospital_app.tests.ConfigurationTests import ConfigurationTest


class TestEmployeeViews(ConfigurationTest):
    """
    This is the class for employee views test cases
    """

    def test_employees(self):
        """
        Tests whether the get request on employees page works correctly,
        returning the status code 200
        """
        response = self.app.get('/employees')
        self.assertEqual(200, response.status_code)

    def test_wrong_date_args(self):
        """
        Tests whether the get request on employees page with success=false param
        works correctly, returning the status code 302
        """
        response = self.app.get('/employees?success=false')
        self.assertEqual(302, response.status_code)

    def test_add_employee(self):
        """
        Tests whether the get request on add employee page works correctly,
        returning the status code 200
        """
        response = self.app.get('/employees/add')
        self.assertEqual(200, response.status_code)

    def test_employee_added(self):
        """
        Tests whether the get request on add employee page works correctly,
        and redirects to employees page, returning the status code 302
        """
        response = self.app.get('/employees/add?added=true')
        self.assertEqual(302, response.status_code)

    def test_employee_not_added(self):
        """
        Tests whether the get request on add employee page works correctly,
        and redirects to employee page, returning the status code 302
        """
        response = self.app.get('/employees/add?added=false')
        self.assertEqual(302, response.status_code)

    def test_edit_employee(self):
        """
        Tests whether the get request on edit employee page works correctly,
        returning the status code 200
        """
        date = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        employee = Employee(name="name1", salary=100, date_of_birth=date)
        database.session.add(employee)
        database.session.commit()
        response = self.app.get('/employees/edit/1')
        self.assertEqual(200, response.status_code)

    def test_employee_edited(self):
        """
        Tests whether the get request on edit employee page works correctly,
        and redirects to employees page, returning the status code 302
        """
        date = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        employee = Employee(name="name1", salary=100, date_of_birth=date)
        database.session.add(employee)
        database.session.commit()
        response = self.app.get('/employees/edit/1?edited=true')
        self.assertEqual(302, response.status_code)

    def test_employee_not_edited(self):
        """
        Tests whether the get request on edit employee page works correctly,
        and redirects to employee page, returning the status code 302
        """
        date = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        employee = Employee(name="name1", salary=100, date_of_birth=date)
        database.session.add(employee)
        database.session.commit()
        response = self.app.get('/employees/edit/1?edited=false')
        self.assertEqual(302, response.status_code)

    def test_delete_employee(self):
        """
        Tests whether the get request on delete employee page works correctly,
        returning the status code 200
        """
        date = datetime.strptime('02/23/1997', '%m/%d/%Y').date()
        employee = Employee(name="name1", salary=210, date_of_birth=date)
        database.session.add(employee)
        database.session.commit()
        response = self.app.get('/employees/delete/1')
        self.assertEqual(302, response.status_code)
