.. role:: bash(code)
    :language: bash


===========
Development
===========
Should you want to contribute to this role, or if you intend to fork it and change
it to suit your needs, this document should get you up to speed and ready to work on it.

============
Requirements
============
In order to contribute to this module you will need to have the following components installed
on your system:

- Python
- Pip
- Virtualenv
- Git

=========================================
Isolate the development environment first
=========================================
Once you have every tool needed in place you will need to prepare the virtual environment: ::

$ virtualenv venv
$ source venv/bin/<your_shell_activate_script>

**Note:** you need to change `<your_shell_activate_script>` with the name of the `activate` appropriate for your shell. For example, if you are using the `fish` shell, the script should be `activate.fish`.

Once your virtual environment is ready, you can install the project dependencies like so: ::

$ pip install -r requirements.txt

==========================
Make sure lights are green
==========================
You should be ready by now but before you start changing files around, please make sure all the project unit and integration tests pass.
Run the unit tests first: ::

$ python -m unittest discover -f

Then run the integration tests: ::

$ behave

If you don't get any error (I strive not to leave the project in a "red state", but hey..), then it means you can FINALLY start!

**Important note:** if you're willing to do a major overhaul of the current project's structure and/or functionalities, please start a conversation first. It might save you from doing work which might not be merged!

=======
License
=======
Please see the LICENSE file for more information.