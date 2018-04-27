This is a repository for wrapping applications for Orion Cubes.  Is may be modified 
to wrap an application.  The layout is as follows

  * README.md : Readme file intended for the users of this repository
  * README_developer.md : Readme file for the developer of this repository
  * {{cookiecutter.repo_name}}/ : Subdirectory where the executable files should be placed
  * {{cookiecutter.repo_name}}/__init__.py : The file containing the python wrapper
  * tests/ : Subdirectory for unit tests
  * docs/ : Subdirectory for documentation
  * setup.py : Python file that manages making this repository a python package
  * requirements.txt : Requirements file for developers of this repository
  * manifest.json : JSON file that manages making this a valid orion package
  * orion_requirements.txt : Orion configuration file specifying the requirements of this package
  

# Development Environment Setup

This repository should be developed with python 3.5.  It is good practice to do so
within a virtual environment.  Once you've installed your virtual environment you
can setup development of this package by invoking this command from the root directory
of this repository

    pip install -U -r requirements.txt
    
Note that you must have your pip.conf and .pypirc configured to allow access to
magpie.eyesopen.com to be able to install the required packages above.  

Example pip.conf

    [global]
    extra-index-url = https://magpie.eyesopen.com/simple/ 

# Skeleton application and wrapper

When initially created from cookiecutter the skeleton contains only a framework for the wrapper as follows
 
  * {{cookiecutter.repo_name}}/__init__.py : A template for python code to expose your application as a function
  * tests/test_myappapi.py : A template for a unit test for the wrapper function
  * docs/source/app_api.rst : A template for the documentation of the python api point

The intention is that you will carry out each of these three tasks following the more detailed help that follows.

  #. Put a Ubuntu 14 compatible version of your application into the {{cookiecutter.repo_name}} directory

  #. Modify each of the associated template files to wrap, document, test and package your application

  #. Build a pip package using ``invoke package`` and upload it to an Orion accessible pypi server

# Running tests

To run the cube unit test(s) run the following command from the root directory of this
repository.

    pytest .

# Creating a package for Orion or python

To create a python or orion package from this repository use the following command from
root directory of this repository.

    invoke package
    
The place will be placed in the dist/ directory

# Creating documentation

To auto generate html documentation from the documentation built into the cubes you've
created run the following command from the root directory of this repository.

    invoke docs

# Updating the version of your repository

To update the version of your repository, change the __version__ variable in the
{{cookiecutter.repo_name}}/__init__.py file.  Note that the version should always
be of the form "<major version number>.<minor version number>.<bugfixnumber>".

# Adding requirements
Once you've created the template if you have additional python package requirements
for this repository add them to the requirements list variable in setup.py.

setup.py requirements variable declaration

    requirements = ["OpenEye-cuberecord", "OpenEye-snowball>=0.10.5", "numpy"]
    
# Edit the README.md

Once you a finished creating your repository write a description of what is
in the repository to the README.md file.

Example .pypirc

    [distutils]
    index-servers = magpie
    
    [magpie]
    repository: https://magpie.eyesopen.com/simple/
    username: <obtain your username from OpenEye>
    password: <obtain your password from OpenEye>


