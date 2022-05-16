from model.group import Group
from random import randrange


def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test1", footer="group for test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.delete.group_by_index(index)
    assert (len(old_groups) - 1) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups
    app.navigation.return_to_homepage()