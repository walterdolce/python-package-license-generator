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

from license_generator.agplv3_transliterator import AGPLv3Transliterator
from license_generator.transliterable import Transliterable


class TestAGPLv3Transliterator(unittest.TestCase):
    def test_it_returns_the_expected_transliterated_bundled_license_filename(self):
        expected_license_filename = 'agpl30'
        transliterables = ['agpl30', 'AGPLv3', 'agplv3']
        for transliterable in transliterables:
            transliterator = AGPLv3Transliterator()
            transliterated = transliterator.transliterate(Transliterable(transliterable))
            self.assertEquals(transliterated.get_transliterable(), expected_license_filename)


if __name__ == '__main__':
    unittest.main()
