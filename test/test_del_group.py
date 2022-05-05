from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test1", footer="group for test"))
    app.delete.first_group()
    app.navigation.return_to_homepage()
