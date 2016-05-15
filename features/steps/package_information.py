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
import subprocess
import license_generator
import os
from behave import *


def assert_command_output_presence(context):
    """Verifies whether the context has the command_output attribute set."""
    if not context.command_output:
        raise RuntimeError('The context has no command_output attribute set.')


@when(u'I run the license-generator "{command_name}" command')
def step_impl(context, command_name):
    os.chdir(context.testing_ground_path)
    context.command_output = subprocess.check_output(
        license_generator.__command_format__.format(command_name=command_name),
        shell=True
    )
    os.chdir(context.base_path)


@then(u'I should see its name')
def step_impl(context):
    assert_command_output_presence(context)
    assert (context.command_output.split(os.linesep)[0].split(' ')[0] == 'license-generator')


@then(u'I should see its version')
def step_impl(context):
    assert_command_output_presence(context)
    assert (context.command_output.split(os.linesep)[0].split(' ')[1] == license_generator.__version__)


@then(u'I should see its copyright notice')
def step_impl(context):
    assert_command_output_presence(context)
    assert (context.command_output.split(os.linesep)[1] == license_generator.__copyright_notice__)


@then(u'I should see its legal status')
def step_impl(context):
    assert_command_output_presence(context)
    command_output_lines = context.command_output.split(os.linesep)
    command_output_lines.remove('')
    command_output_lines.pop(0)
    command_output_lines.pop(0)
    assert (os.linesep.join(command_output_lines) == license_generator.__legal_status__)
