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


class LicenseFileLocator(object):
    def locate(self, license_name):
        license_name = license_name.lower()
        license_path = os.path.join(os.path.dirname(__file__), 'licenses', license_name)
        print license_path
        if not os.path.exists(license_path):
            raise IOError(
                'License "{license_path}" does not exist.'.format(license_path=license_path)
            )
        return license_path
