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
import license_generator
import os
from behave import *


@when(u'I run the license-generator "{command_name}" command')
def step_impl(context, command_name):
    context.run_command(command_name)


@when(u'I run the license-generator "{command_name}" command with no arguments')
def step_impl(context, command_name):
    try:
        context.run_command(command_name)
    except Exception as e:
        pprint.pprint(context.__dict__)
        if hasattr(e, 'returncode'):
            context.returncode = e.returncode
        if hasattr(e, 'output'):
            context.command_output = e.output
    finally:
        pass


@then(u'I should see its name')
def step_impl(context):
    context.assert_command_output_presence()
    assert (context.command_output.split(os.linesep)[0].split(' ')[0] == 'license-generator')


@then(u'I should see its version')
def step_impl(context):
    context.assert_command_output_presence()
    assert (context.command_output.split(os.linesep)[0].split(' ')[1] == license_generator.package_info.__version__)


@then(u'I should see its copyright notice')
def step_impl(context):
    context.assert_command_output_presence()
    assert (context.command_output.split(os.linesep)[1] == license_generator.package_info.__copyright_notice__)


@then(u'I should see its legal status')
def step_impl(context):
    context.assert_command_output_presence()
    command_output_lines = context.command_output.split(os.linesep)
    command_output_lines.remove('')
    command_output_lines.pop(0)
    command_output_lines.pop(0)
    assert (os.linesep.join(command_output_lines) == license_generator.package_info.__legal_status__)


@when(u'I run the license-generator')
def step_impl(context):
    context.run_command('')


@then(u'I should see the usage info')
def step_impl(context):
    context.assert_command_output_presence()
    assert (context.command_output == license_generator.package_info.__usage_info__ + os.linesep)
