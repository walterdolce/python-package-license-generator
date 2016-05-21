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
from license_generator.file_generator import FileGenerator
from license_generator.file_locator import FileLocator
from license_generator.package.info import __usage_info__ as usage_info
from license_generator.package.info import __version_info__ as version_info
from license_generator.agplv3_transliterator import AGPLv3Transliterator
from license_generator.apache2_transliterator import Apache2Transliterator
from license_generator.gplv3_transliterator import GPLv3Transliterator
from license_generator.lgplv3_transliterator import LGPLv3Transliterator
from license_generator.license_file_generator import LicenseFileGenerator
from license_generator.license_file_locator import LicenseFileLocator
from license_generator.mit_transliterator import MitTransliterator
from license_generator.mplv2_transliterator import MPLv2Transliterator
from license_generator.transliterable import Transliterable
from license_generator.unlicense_transliterator import UnlicenseTransliterator
from license_generator.package.messages import __no_license_generated__ as no_license_generated_message


class LicenseGenerator(object):
    _file_locator = None
    _file_generator = None

    def __init__(self, file_locator=FileLocator, file_generator=FileGenerator):
        self._file_locator = file_locator
        self._file_generator = file_generator

    def help(self):
        self.run_command('help')

    def generate(self, license_name=None, destination_dir=None):
        if not license_name:
            self._exit_with_message(no_license_generated_message, code=1)

        license_name = self._transliterate_license_name(license_name)
        license_name = self._file_locator.locate(license_name)
        license_path = self._compute_license_path(destination_dir)

        self._file_generator.generate(license_name, license_path)

    def _compute_license_path(self, destination_dir=None):
        license_path = None
        if destination_dir:
            if not os.path.exists(os.path.abspath(destination_dir)):
                raise IOError(
                    'Directory {directory} does not exist.'.format(
                        directory=os.path.abspath(destination_dir)
                    )
                )
            license_path = os.path.abspath(destination_dir)
        return license_path

    def _transliterate_license_name(self, license_name):
        agplv3_transliterator = AGPLv3Transliterator()
        apache_transliterator = Apache2Transliterator()
        gplv3_transliterator = GPLv3Transliterator()
        lgplv3_transliterator = LGPLv3Transliterator()
        mit_transliterator = MitTransliterator()
        mplv2_transliterator = MPLv2Transliterator()
        unlicense_transliterator = UnlicenseTransliterator()
        mplv2_transliterator.set_successor(unlicense_transliterator)
        mit_transliterator.set_successor(mplv2_transliterator)
        lgplv3_transliterator.set_successor(mit_transliterator)
        gplv3_transliterator.set_successor(lgplv3_transliterator)
        apache_transliterator.set_successor(gplv3_transliterator)
        agplv3_transliterator.set_successor(apache_transliterator)
        transliterable = agplv3_transliterator.transliterate(
            Transliterable(license_name)
        )
        return transliterable.get_transliterable()

    def run_command(self, *args):
        args = args[0]

        if len(args) < 1:
            self.help()

        try:
            command = args[1]
        except IndexError:
            command = 'help'

        destination_dir = None
        enumerated_args = enumerate(args)
        for (index, argument) in enumerated_args:
            if argument == '--destination-dir':
                try:
                    destination_dir = enumerated_args.next()[1]
                except StopIteration:
                    destination_dir = None
                finally:
                    if destination_dir is not None:
                        break

        if command == 'help':
            self._exit_with_message(usage_info)
        if command == 'version':
            self._exit_with_message(version_info)
        if command == 'generate':
            try:
                license_name = args[2]
            except IndexError:
                license_name = None
            self.generate(license_name, destination_dir)

    def _exit_with_message(self, message, code=0):
        print(message)
        exit(code)
