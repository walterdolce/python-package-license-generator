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
from behave import *


@given(u'license-generator is installed on the system')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given license-generator is installed on the system')


@when(u'I run license-generator\'s "generate" command with "MIT" as argument')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I run license-generator\'s "generate" command with "MIT" as argument')


@then(u'the "LICENSE" file is generated')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the "LICENSE" file is generated')


@then(u'the "LICENSE" file contains the "MIT" license')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the "LICENSE" file contains the "MIT" license')
