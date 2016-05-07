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
from license_generator.chainable_transliterator import ChainableTransliterator
from license_generator.transliterable import Transliterable


class UnlicenseTransliterator(ChainableTransliterator):
    _license_filename = 'unlicense'
    _transliterables = ['unlicense']

    def transliterate(self, transliterable=Transliterable):
        raw_transliterable = transliterable.get_transliterable()
        raw_transliterable = raw_transliterable.lower()
        if raw_transliterable in self._transliterables:
            transliterable.set_transliterable(transliterable=self._license_filename)
            transliterable.set_is_transliterated(True)
        if self.successor is not None and transliterable.is_transliterated() is not True:
            transliterable = self.successor.transliterate(transliterable)
        return transliterable
