from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test1", footer="group for test"))
    old_groups = app.group.get_group_list()
    group = Group(number_of_group=1, name="Group of 4")
    group.id = old_groups[0].id
    app.modify.group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    app.navigation.return_to_homepage()
