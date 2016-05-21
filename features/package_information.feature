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
Feature: Package information
  In order to know more about the license-generator package
  As a user
  I want to be able to get relevant information about the package from the package itself

  Background:
    Given the license-generator package is installed on the system

  Scenario: User asks for package version information
    When I run the license-generator "version" command
    Then I see its name
    And I see its version
    And I see its copyright notice
    And I see its legal status

  Scenario: User doesn't send any command
    When I run the license-generator
    Then I see its usage info

  Scenario: User asks for usage info
    When I run the license-generator "help" command
    Then I see its usage info