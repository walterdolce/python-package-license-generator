.. image:: https://travis-ci.org/walterdolce/python-package-license-generator.svg?branch=master
    :target: https://travis-ci.org/walterdolce/python-package-license-generator
.. _GNU Coding Standards: https://www.gnu.org/prep/standards/html_node/_002d_002dversion.html

=================
license-generator
=================
The ``license-generator`` is a simple CLI tool which allows you to create LICENSE files.
The tool ships with the most common types of licenses used in the software industry. The list of licenses
available can be found in the ``license_generator/licenses/`` folder.

Please note the package is undergoing development so you **may** find bugs or see ugly output.

Usage
-----
To generate a license, run the command by specifying the license name as shown below.
Example: ::

    $ license-generator generate MIT


Commands Available
------------------

+ **generate**: generates a LICENSE file from the license name specified.
+ **help**: shows usage info.
+ **version**: shows package version, copyright notice and legal status (as defined by the `GNU Coding Standards`_)

============
Contributing
============

Please see the DEVELOPMENT.rst file for more information.

=======
License
=======
Please see the LICENSE file for more information.