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
from license_generator.package.info import __version__ as package_version
from license_generator.package.info import __copyright_notice__ as package_copyright_notice
from license_generator.package.info import __legal_status__ as package_legal_status
from license_generator.package.info import __usage_info__ as package_usage_info
import os
from behave import *


@when(u'I run the license-generator "{command_name}" command')
def step_impl(context, command_name):
    context.assert_license_generator_existence()
    context.run_command('license-generator {command}'.format(command=command_name))


@when(u'I run the license-generator "{command_name}" command with no arguments')
def step_impl(context, command_name):
    context.assert_license_generator_existence()
    try:
        context.run_command('license-generator {command}'.format(command=command_name))
    except Exception as e:
        if hasattr(e, 'returncode'):
            context.returncode = e.returncode
        if hasattr(e, 'output'):
            context.command_output = e.output


@then(u'I see its name')
def step_impl(context):
    context.assert_command_output_presence()
    assert (context.command_output.split(os.linesep)[0].split(' ')[0] == 'license-generator')


@then(u'I see its version')
def step_impl(context):
    context.assert_command_output_presence()
    assert (context.command_output.split(os.linesep)[0].split(' ')[1] == package_version)


@then(u'I see its copyright notice')
def step_impl(context):
    context.assert_command_output_presence()
    assert (context.command_output.split(os.linesep)[1] == package_copyright_notice)


@then(u'I see its legal status')
def step_impl(context):
    context.assert_command_output_presence()
    command_output_lines = context.command_output.split(os.linesep)
    command_output_lines.remove('')
    command_output_lines.pop(0)
    command_output_lines.pop(0)
    assert (os.linesep.join(command_output_lines) == package_legal_status)


@when(u'I run the license-generator')
def step_impl(context):
    context.assert_license_generator_existence()
    context.run_command('license-generator')


@then(u'I see its usage info')
def step_impl(context):
    context.assert_command_output_presence()
    assert (context.command_output.strip() == package_usage_info)
