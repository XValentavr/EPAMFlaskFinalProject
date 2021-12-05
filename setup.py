from setuptools import setup, find_packages

setup(
    name='Hospital application',
    version='1.0',
    author='Valentyn Volynskiy',
    author_email='iwilly17@gmail.com',
    description='Web application to demostrate hospital departments and employees using web server',
    url='https://github.com/XValentavr/FlaskHospitalApp',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask == 2.0.2',
        'Flask_Login == 0.5.0',
        'Flask_Migrate == 3.1.0',
        'Flask_RESTful == 0.3.9',
        'Flask_SQLAlchemy == 2.5.1',
        'Flask_WTF == 1.0.0',
        'SQLAlchemy == 1.4.27',
        'Werkzeug == 2.0.2',
        'WTForms == 3.0.0',
    ]
)
