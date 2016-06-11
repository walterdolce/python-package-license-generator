#!/usr/bin/env python
#
#    license-generator
#    Copyright (C) 2016  Walter Dolce <walterdolce@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from sys import path as sys_path
from sys import exit
from os import path as os_path
from codecs import open

try:
    from setuptools import setup
except ImportError:
    print(
        "license-generator needs setuptools in order to build."
        "Install it using your package manager (usually python-setuptools)"
        "or via pip (pip install setuptools)."
    )
    exit(1)

sys_path.insert(0, os_path.abspath('license_generator'))

from license_generator.package.info import __version__ as version
from license_generator.package.info import __author__ as author
from license_generator.package.info import __author_email__ as author_email

with open(os_path.join(os_path.abspath(os_path.dirname(__file__)), 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='license_generator',
    version=version,
    author=author,
    author_email=author_email,
    description='A command line tool for generating license files',
    long_description=long_description,
    license='GPLv3',
    keywords='license generator cli utility tool file licenses generators utilities files tools',
    packages=['license_generator'],
    scripts=[
        'bin/license-generator'
    ],
    test_suite='test',
    url='https://github.com/walterdolce/python-package-license-generator',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GPLv3',
        'Programming Language :: Python :: 2.7'
    ]
)
