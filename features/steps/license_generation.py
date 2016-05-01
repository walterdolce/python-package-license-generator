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
from behave import *
import subprocess
import os
from license_generator.exceptions import FileGenerationError


@given(u'the license-generator package is installed on the system')
def step_impl(context):
    subprocess.check_output(
        'python {base_path}/setup.py develop'.format(base_path=context.base_path),
        shell=True
    )
    subprocess.check_call('which license-generator', shell=True)


@when(u'I run the license-generator "{command_name}" command with "{command_parameter}" as argument')
def step_impl(context, command_name, command_parameter):
    os.chdir(context.testing_ground_path)
    subprocess.check_call(
        'license-generator {command_name} {command_parameter}'.format(
            command_name=command_name,
            command_parameter=command_parameter
        ),
        shell=True
    )
    os.chdir(context.base_path)


@then(u'the "{license_filename}" file is generated')
def step_impl(context, license_filename):
    license_file = os.path.join(context.testing_ground_path, license_filename)
    if not os.path.isfile(license_file):
        raise FileGenerationError(
            '{license_file} file was not generated'.format(license_file=license_file)
        )


@then(u'the generated "{license_filename}" file contains the "{license_type}" license')
def step_impl(context, license_filename, license_type):
    generated_license_content = readfile(
        os.path.join(context.testing_ground_path, license_filename)
    )
    builtin_license_content = readfile(
        os.path.join(context.base_path, 'license_generator', 'licenses', license_type.lower())
    )
    assert(builtin_license_content == generated_license_content)


def readfile(license_file):
    with open(license_file, 'r') as f:
        license_file_content = f.read()
    return license_file_content
