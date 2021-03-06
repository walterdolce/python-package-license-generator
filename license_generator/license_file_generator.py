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
from __future__ import print_function
import os
import shutil
from license_generator.file_generator import FileGenerator


class LicenseFileGenerator(FileGenerator):
    def generate(self, license_name=None, license_path=None):
        if not license_path:
            license_path = os.getcwd()
        shutil.copy(license_name, os.path.join(license_path, 'LICENSE'))
        print('License "{license_name}" generated.'.format(license_name=license_name))
