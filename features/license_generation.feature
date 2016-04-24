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
Feature: License generation
  In order to save time when bootstrapping new projects
  As a software engineer
  I want to be able to quickly generate license files

  Scenario: It generate licenses based on license "slug"
    Given license-generator is installed on the system
    When I run license-generator's "generate" command with "MIT" as argument
    Then the "LICENSE" file is generated
    And the "LICENSE" file contains the "MIT" license