from model.contact import Contact
from model.group import Group


def test_add_first_contact_to_group(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Roland", surname="Braund"))
        app.group.create(Group(name="New one"))
    app.contact.add_first_contact_to_group(group_name="New one")
