"""
This module defines the test cases for department service
"""
# standard library imports
from datetime import datetime

# local imports
from hospital_app import database
from hospital_app.models.hospital import Hospital
from hospital_app.models.employee import Employee
from hospital_app.service import departmets_of_hospital
from hospital_app.tests.ConfigurationTests import ConfigurationTest


class TestDepartmentOfHospitalService(ConfigurationTest):
    """
    This is the class for departments of hospital service test cases
    """

    def test_get_all_departments_of_hospital(self):
        """
        Adds  test records and tests the result
        """
        department1 = Hospital(name="department1", to_do="description1")
        department2 = Hospital(name="department2", to_do="description2")
        database.session.add(department1)
        database.session.add(department2)
        database.session.commit()
        self.assertEqual(2, len(departmets_of_hospital.get_hospital_department()))

    def test_add_department_of_hospital(self):
        """
        Adds a new department with specified parameters and tests whether the count
        of records is 1
        """
        departmets_of_hospital.add_department(name="New department", to_do="New description")
        self.assertEqual(1, Hospital.query.count())

    def test_get_department_of_hospital_by_id(self):
        """
        Adds 1 test record and tests whether the id of added record is 1
        """
        department = Hospital(name="department1", to_do="description1")
        database.session.add(department)
        database.session.commit()
        self.assertEqual(1, departmets_of_hospital.get_department_by_id(1)['id'])

    def test_update_department_of_hospital(self):
        """
        Adds a new department with specified parameters, updates it with new parameters
        and tests whether the values updated
        """
        department = Hospital(name="department1", to_do="description1")
        database.session.add(department)
        database.session.commit()
        departmets_of_hospital.update_department(1, name="new name", to_do="new description")
        department = Hospital.query.get(1)
        self.assertEqual("new name", department.name)
        self.assertEqual("new description", department.to_do)

    def test_delete_department_of_hospital(self):
        """
        Adds a new department with specified parameters, deletes it and tests
        whether the count of records is 0
        """
        department = Hospital(name="department1", to_do="description1")
        database.session.add(department)
        database.session.commit()
        departmets_of_hospital.delete_department(1)
        self.assertEqual(0, Hospital.query.count())

    def test_show_department_of_hospital(self):
        """
        Adds 1 test record and tests whether the string representation of
        department is correct
        :return:
        """
        department = Hospital(name="department1", to_do="description1")
        database.session.add(department)
        database.session.commit()
        self.assertEqual('<Hospital: department1>', repr(department))

    def test_get_average_salary(self):
        """
        Adds a department and a few employees and tests whether the average salary
        has an expected value
        """
        department = Hospital(name="department1", to_do="description1")
        database.session.add(department)
        date1 = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        date2 = datetime.strptime('05/16/1996', '%m/%d/%Y').date()
        employee1 = Employee(name="name1", date_of_birth=date1,
                             salary=1500, hospital_id=1)
        employee2 = Employee(name="second-name", date_of_birth=date2,
                             salary=2500, hospital_id=1)
        database.session.add(employee1)
        database.session.add(employee2)
        database.session.commit()
        self.assertEqual(2000, departmets_of_hospital.get_average_salary(department.json()))
