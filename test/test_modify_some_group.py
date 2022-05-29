from model.group import Group
from random import randrange


def test_modify_some_group(app, db, check_ui, data_group):
    group = data_group
    if len(db.get_group_list()) == 0:
        app.group.create(group)
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group.number_of_group = old_groups[index].number_of_group
    app.modify.group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
    app.navigation.return_to_homepage()
