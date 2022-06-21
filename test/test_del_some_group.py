from model.group import Group
import random
import allure


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test1", footer="group for test"))
    with allure.step('Given non-empty group list'):
        old_groups = db.get_group_list()
    with allure.step('Given random group from the list'):
        group = random.choice(old_groups)
    with allure.step('When I delete a group %s from the list' % group):
        app.delete.group_by_id(group.number_of_group)
        assert (len(old_groups) - 1) == app.group.count()
    with allure.step('Then the new group list is equal to the old list without the deleted group'):
        new_groups = db.get_group_list()
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
        app.navigation.return_to_homepage()
