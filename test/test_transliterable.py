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
from license_generator.transliterable import Transliterable


class TestTransliterable(unittest.TestCase):
    def test_it_is_not_transliterated_by_default(self):
        transliterable = Transliterable('foo')
        self.assertFalse(transliterable.is_transliterated())

    def test_it_returns_the_transliterable_word(self):
        transliterable = Transliterable('foo')
        self.assertEquals(transliterable.get_transliterable(), 'foo')

    def test_it_changes_the_transliterable_word(self):
        transliterable = Transliterable('foo')
        transliterable.set_transliterable('bar')
        self.assertEquals(transliterable.get_transliterable(), 'bar')

    def test_it_returns_the_transliteration_status_once_its_set(self):
        transliterable = Transliterable('foo')
        transliterable.set_is_transliterated(True)
        self.assertTrue(transliterable.is_transliterated())
