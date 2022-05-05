from model.contact import Contact
from model.group import Group


def test_add_all_contacts_to_group(app):
    if app.contact.count() <= 1:
        app.contact.create(Contact(name="Roland", surname="Braund"))
        app.contact.create(Contact(name="Voland", surname="Round"))
        app.group.create(Group(name="New one"))
        app.navigation.return_to_homepage()
    app.contact.add_all_contacts_to_group(group_name="New one")

