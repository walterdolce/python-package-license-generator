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

  Scenario Outline: It generates licenses based on their name
    Given the license-generator package is installed on the system
    When I run the license-generator "generate" command with "<license_type>" as argument
    Then the "LICENSE" file is generated
    And the generated "LICENSE" file contains the "<license_type_code>" license

    Examples:
      | license_type | license_type_code |
      | AGPLv3       | agpl30            |
      | agplv3       | agpl30            |
      | AGPL30       | agpl30            |
      | agpl30       | agpl30            |
      | APACHE20     | apache20          |
      | apache20     | apache20          |
      | GPL30        | gpl30             |
      | gpl30        | gpl30             |
      | LGPL30       | lgpl30            |
      | lgpl30       | lgpl30            |
      | MIT          | mit               |
      | mit          | mit               |
      | MPL20        | mpl20             |
      | mpl20        | mpl20             |
      | UNLICENSE    | unlicense         |
      | unlicense    | unlicense         |

  Scenario: Generate command fails if no license is specified
    Given the license-generator package is installed on the system
    When I run the license-generator "generate" command with no arguments
    Then I will be remainded to specify a license name
    And the program will exit with an error code

  Scenario: It generates the license in the specified location
    Given the license-generator package is installed on the system
    And the directory "some/project" exists
    When I run "license-generator generate MIT --destination-dir 'some/project'
    Then the "some/project/LICENSE" file is generated
    And the generated "some/project/LICENSE" file contains the "mit" license