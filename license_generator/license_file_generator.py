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
import shutil

from license_generator.file_generator import FileGenerator
from license_generator.file_locator import FileLocator


class LicenseFileGenerator(FileGenerator):
    _locator = None

    def __init__(self, locator=FileLocator):
        self._locator = locator

    def generate(self, license_name):
        license_file = self._locator.locate(license_name)
        shutil.copy(
            license_file,
            os.path.join(os.getcwd(), 'LICENSE')
        )
        pass
