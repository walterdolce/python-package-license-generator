.. image:: https://travis-ci.org/walterdolce/python-package-license-generator.svg?branch=master
    :target: https://travis-ci.org/walterdolce/python-package-license-generator

=================
license-generator
=================
The ``license-generator`` is a simple CLI tool which allows you to create LICENSE files in a single command.
The tool ships with the most common types of licenses used in the software industry. The list of available
licenses can be found in the ``license_generator/licenses/`` folder.

The package is undergoing development so you **may** find bugs. The only command currently available is ``generate``,
which, as you might guess, will generate the license you will specify.

Usage
-----
To generate a license, run the command by specifying the license name as shown below.
Example: ::

    $ license-generator generate MIT


Commands Available
------------------

+ **generate**: generates a LICENSE file from the license name specified after the command.
+ **version**: prints package version, copyright and brief license information.

============
Contributing
============

Please see the DEVELOPMENT.rst file for more information.

=======
License
=======
Please see the LICENSE file for more information.