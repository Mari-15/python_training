from model.group import Group
from random import randrange


def test_modify_some_group(app, data_group):
    group = data_group
    if app.group.count() == 0:
        app.group.create(group)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group.number_of_group = old_groups[index].number_of_group
    app.modify.group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    app.navigation.return_to_homepage()
