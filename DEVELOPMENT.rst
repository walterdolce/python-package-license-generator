.. image:: https://travis-ci.org/walterdolce/python-package-license-generator.svg?branch=master
    :target: https://travis-ci.org/walterdolce/python-package-license-generator
.. _Requirements for Installing Packages: https://packaging.python.org/en/latest/installing/#installing-requirements

===========
Development
===========
Should you want to contribute to this package, or should you intend to fork it and change
it to suit your needs, this document should get you up to speed and ready to work on it.

============
Requirements
============
In order to contribute to this package, you will need to have the following components installed
on your system:

- Python (I started working on the package with Python 2.7.10)
- Pip (I started working on the package with pip 8.1.1)
- Virtualenv
- Git

======================================
Preparing your development environment
======================================
Before jumping straight to code, you might need to prepare your development environment first.
In order to do that, I suggest to have a read at the `Requirements for Installing Packages`_ page from the Python
Packaging User Guide.

You should find information on how to install ``pip``, ``setuptools``, ``wheels`` and ``virtualenv``.

=========================================
Isolate the development environment first
=========================================
Once you have what's needed in place, you will have to prepare the virtual environment: ::

$ virtualenv venv
$ source venv/bin/<your_shell_activate_script>

**Note:** you need to change ``<your_shell_activate_script>`` with the name of the ``activate`` script appropriate for your shell. For example, if you are using the ``fish`` shell, the script should be ``activate.fish``.

Once your virtual environment is ready, you can install the project dependencies like so: ::

$ pip install -r requirements.txt

==========================
Make sure lights are green
==========================
You should have everything you need by now. Before you start changing files around though, please make sure all the project's unit and integration tests pass.
First, run the unit tests: ::

$ python -m unittest discover -f

Then run the integration tests: ::

$ behave

If you don't get any error (I strive not to leave the project in a "red state", but hey!), then it means you can FINALLY start!

**Important note:** if you're willing to do a major overhaul of the current project's structure and/or a new feature which require you to make a lot of changes, please start a conversation first. It might save you from doing work which might not be merged! The best way to do it is to open an issue here on GitHub or, if you want to keep things private, send
 me an email.

=======
License
=======
Please see the LICENSE file for more information.