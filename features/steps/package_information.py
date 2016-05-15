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
import pprint
import subprocess
from collections import deque

import license_generator
import os
from behave import *


@when(u'I run the license-generator "{command_name}" command')
def step_impl(context, command_name):
    os.chdir(context.testing_ground_path)
    context.command_output = subprocess.check_output(
        'license-generator {command_name}'.format(command_name=command_name),
        shell=True
    )
    os.chdir(context.base_path)


@then(u'I should see its name')
def step_impl(context):
    assert_command_output_presence(context)
    command_output = context.command_output.split(os.linesep)
    command_output = command_output[0].split(' ')
    assert (command_output[0] == 'license-generator')


def assert_command_output_presence(context):
    if not context.command_output:
        raise RuntimeError(
            'Expected command output set within the step definition context but none found.'
        )


@then(u'I should see its version')
def step_impl(context):
    assert_command_output_presence(context)
    command_output = context.command_output.split(os.linesep)
    command_output = command_output[0].split(' ')
    assert (command_output[1] == license_generator.__version__)


@then(u'I should see its copyright notice')
def step_impl(context):
    assert_command_output_presence(context)
    command_output = context.command_output.split(os.linesep)
    version = license_generator.__copyright_short__
    assert (command_output[1] == version)


@then(u'I should see its legal status')
def step_impl(context):
    assert_command_output_presence(context)
    command_output = context.command_output.split(os.linesep)
    command_output.pop(0)
    command_output.pop(0)
    license_info = """License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
"""
    print(os.linesep.join(command_output))
    assert (os.linesep.join(command_output) == license_info)
