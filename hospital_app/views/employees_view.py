"""
This module represents the logic on routes starting with /employees
"""
from flask import render_template, redirect, flash, url_for, request
from . import user


@user.route('/employees', methods=["POST", "GET"])
def get_employees():
    return render_template('employees_of_hospital/employees.html')


@user.route('/employees/delete/<int:identifier>', methods=['GET', 'POST'])
def delete_employee(identifier):
    """
    This function represents the logic on /employees/delete address
    :return: the rendered employees.html template with deleted employee
    """
    # form a flash message
    flash('You have successfully deleted the employee.')

    # redirect to employees.html after the element is deleted
    return redirect(url_for('user.get_employees'))


@user.route('/employees/add', methods=['GET'])
def add_employee():
    """
    This function represents the logic on /employees/add address
    :return: the rendered employee.html template to add a new employee
    """
    # declare a flag variable which indicates which title to load 'Add' or 'Edit' at employee.html
    flag = True

    # get the added argument if the form is submitted
    added = request.args.get("added")

    if added is not None and added == 'true':
        # form a flash message
        flash('You have successfully added the employee.')

        # redirect to employees.html after the element is added
        return redirect(url_for('user.get_employees'))
    if added is not None and added == 'false':
        # form a flash message
        flash('Couldn\'t add the employee. Missing or invalid data', 'error')

        # redirect to department.html to enter the data again
        return redirect(url_for('user.add_employee'))

    # load employee.html template
    return render_template('employees_of_hospital/employee.html', flag=flag, title="Add employee")


@user.route('/employees/edit/<int:identifier>', methods=['GET'])
def edit_employee(identifier):
    """
    This function represents the logic on /employees/edit address
    :return: the rendered employee.html template to edit an existing employee
    """
    # set add to False to display the 'Edit' title on employee.html
    flag = False

    # get the edited argument if the form is submitted
    edited = request.args.get("edited")

    if edited is not None and edited == 'true':
        # form a flash message
        flash('You have successfully edited the employee.')

        # redirect to employees.html after the element is edited
        return redirect(url_for('user.get_employees'))
    if edited is not None and edited == 'false':
        # form a flash message
        flash('Couldn\'t edit the employee. Missing or invalid data', 'error')

        # redirect to employee.html to enter the data again
        return redirect(url_for('user.edit_employee', identifier=identifier))

    # load employee.html template
    return render_template('employees_of_hospital/employee.html', flag=flag, title="Edit employee")
