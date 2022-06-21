Scenario Outline: Add new group
  Given group list
  Given group with <name>, <header> and <footer>
  When I add the group to the list
  Then the new group list is equal to the old list with the added group

  Examples:
  | name  | header  | footer  |
  | name1 | header1 | footer1 |
  | name2 | header2 | footer2 |


Scenario: Delete a group
  Given non-empty group list
  Given random group from the list
  When I delete the group from the list
  Then the new group list is equal to the old list without the deleted group
