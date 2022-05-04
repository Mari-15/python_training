from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(number_of_group=None, name="Test1", header="Test2", footer="group for test"))
    app.delete.first_group()
