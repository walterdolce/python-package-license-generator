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
from setuptools import setup

setup(
    name='license_generator',
    version='0.1.0',
    author='Walter Dolce',
    author_email='walterdolce@gmail.com',
    description='A command line tool for generating license files',
    license='GPLv3',
    keywords='license generator cli utility file licenses generators utilities files',
    packages=['license_generator'],
    scripts=[
        'bin/license-generator'
    ]
)
