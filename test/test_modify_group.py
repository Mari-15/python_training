from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test1", footer="group for test"))
    app.modify.group(Group(number_of_group=1, name="Group of 4"))
    app.navigation.return_to_homepage()
