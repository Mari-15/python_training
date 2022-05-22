from model.contact import Contact
from model.group import Group


def test_add_all_contacts_to_group(app):
    if app.contact.count() <= 1:
        app.contact.create(Contact(name="Roland", surname="Braund"))
        app.contact.create(Contact(name="Voland", surname="Round"))
    name = Group(name="Check")
    groups = app.group.get_group_list()
    if name not in groups:
        app.group.create(Group(name=name.name))
    app.navigation.return_to_homepage()
    app.contact.add_all_contacts_to_group(group_name=name.name)

