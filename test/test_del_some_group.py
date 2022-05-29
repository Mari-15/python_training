from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test1", footer="group for test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.delete.group_by_id(group.number_of_group)
    assert (len(old_groups) - 1) == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
    app.navigation.return_to_homepage()
