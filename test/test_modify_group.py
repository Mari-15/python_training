from model.group import Group


def test_modify_group(app):
    app.modify.group(Group(number_of_group=1, name="Group of 4"))
