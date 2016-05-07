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
import unittest
from license_generator.license_file_locator import LicenseFileLocator


class TestLicenseFileLocator(unittest.TestCase):
    def test_it_raises_an_error_when_the_requested_license_does_not_exist(self):
        locator = LicenseFileLocator()
        with self.assertRaises(IOError):
            locator.locate('asd')

    def test_it_returns_the_absolute_path_to_the_requested_license(self):
        locator = LicenseFileLocator()
        license_path = locator.locate('agpl30')
        expected_license_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'license_generator',
            'licenses',
            'agpl30'
        )
        self.assertEqual(license_path, expected_license_path)


if __name__ == '__main__':
    unittest.main()
