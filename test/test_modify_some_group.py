from model.group import Group
import random


def test_modify_some_group(app, db, check_ui, data_group):
    group = data_group
    if len(db.get_group_list()) == 0:
        app.group.create(group)
    old_groups = db.get_group_list()
    group1 = random.choice(old_groups)
    app.modify.group_by_id(group1.number_of_group, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
    app.navigation.return_to_homepage()
