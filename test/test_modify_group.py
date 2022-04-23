from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.modify.modify_group(Group(number_of_group=4, name="Group of 4", header="Real test case", footer="just a group"))
    app.session.logout()
