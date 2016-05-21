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
import shutil
import os
from types import MethodType


def assert_command_output_presence(context):
    """Verifies whether the context has the command_output attribute set."""
    if not hasattr(context, 'command_output'):
        raise RuntimeError('The context has no command_output attribute set.')


def run_command(context, command):
    """Runs a command with subprocess.check_output within the testing ground context."""
    os.chdir(context.testing_ground_path)
    context.command_output = subprocess.check_output(command, shell=True)
    os.chdir(context.base_path)


def assert_license_generator_existence(context):
    """Checks whether the license-generator executable exists."""
    subprocess.check_call('which license-generator', shell=True)


def before_all(context):
    """Adds capabilities to the context object."""
    context.assert_command_output_presence = MethodType(assert_command_output_presence, context)
    context.assert_license_generator_existence = MethodType(assert_license_generator_existence, context)
    context.run_command = MethodType(run_command, context)


def before_feature(context, feature):
    """Prepares the ground for the license file(s) to be created."""
    context.base_path = os.getcwd()
    context.testing_ground_path = os.path.join(context.base_path, 'testing-ground')
    if not os.path.exists(context.testing_ground_path):
        os.mkdir(context.testing_ground_path)


def after_feature(context, feature):
    """Deletes files and directories created for verifying the package behaviour."""
    if os.path.exists(context.testing_ground_path):
        license_file = os.path.join(context.testing_ground_path, 'LICENSE')
        if os.path.exists(license_file):
            os.remove(license_file)
        shutil.rmtree(context.testing_ground_path)
    os.chdir(context.base_path)


def after_scenario(context, scenario):
    """Resets the last command return code assigned to the context to 0 if present."""
    if hasattr(context, 'returncode'):
        context.returncode = 0
