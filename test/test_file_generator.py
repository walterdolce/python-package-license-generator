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
from license_generator.file_generator import FileGenerator


class TestFileGenerator(unittest.TestCase):
    def test_it_raises_an_error_when_its_instantiated_directly(self):
        with self.assertRaises(NotImplementedError):
            FileGenerator()

    def test_it_raises_an_error_when_its_method_is_called(self):
        with self.assertRaises(NotImplementedError):
            erroneous = MissingImplementationGenerator()
            erroneous.generate('erroneous')


class MissingImplementationGenerator(FileGenerator):
    def __init__(self):
        pass


if __name__ == '__main__':
    unittest.main()
