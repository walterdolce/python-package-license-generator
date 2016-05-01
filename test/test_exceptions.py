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
import unittest
import license_generator.exceptions


class TestFileGenerationError(unittest.TestCase):
    def test_it_raises_exception_with_the_passed_message(self):
        error_message = 'error!'
        file_generation_error = license_generator.exceptions.FileGenerationError(error_message)
        with self.assertRaises(license_generator.exceptions.FileGenerationError):
            raise file_generation_error
        self.assertEquals(error_message, str(file_generation_error))


if __name__ == '__main__':
    unittest.main()
