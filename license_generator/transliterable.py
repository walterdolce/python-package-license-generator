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


class Transliterable(object):
    _transliterable = None
    _isTransliterated = False

    def __init__(self, transliterable=None):
        self._transliterable = str(transliterable)

    def set_transliterable(self, transliterable=None):
        self._transliterable = str(transliterable)

    def get_transliterable(self):
        return self._transliterable

    def set_is_transliterated(self, is_transliterated=False):
        self._isTransliterated = bool(is_transliterated)

    def is_transliterated(self):
        return self._isTransliterated
