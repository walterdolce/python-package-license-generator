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
import os


def before_feature(context, feature):
    """
    Prepares the ground for the license file(s) to be created.
    """
    context.base_path = os.getcwd()
    context.testing_ground_path = os.path.join(context.base_path, 'testing-ground')
    if not os.path.exists(context.testing_ground_path):
        os.mkdir(context.testing_ground_path)


def after_feature(context, feature):
    """
    Clears everything up.
    """
    if os.path.exists(context.testing_ground_path):
        license_file = os.path.join(context.testing_ground_path, 'LICENSE')
        if os.path.exists(license_file):
            os.remove(license_file)
        os.rmdir(context.testing_ground_path)
    os.chdir(context.base_path)
