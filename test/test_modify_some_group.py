from model.group import Group
from random import randrange


def test_modify_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test1", footer="group for test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Gro54")
    group.number_of_group = old_groups[index].number_of_group
    app.modify.group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    app.navigation.return_to_homepage()
