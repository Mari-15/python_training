from model.contact import Contact
from model.group import Group


def test_add_first_contact_to_group(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Roland", surname="Braund"))
    name = Group(number_of_group=None, name="New one")
    groups = app.group.get_group_list()
    if name not in groups:
        app.group.create(Group(name=name.name))
    app.navigation.return_to_homepage()
    app.contact.add_first_contact_to_group(group_name=name.name)
