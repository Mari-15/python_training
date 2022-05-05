from model.contact import Contact
from model.group import Group


def test_remove_first_contact_from_group(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Roland", surname="Braund"))
    if app.group.count() == 0:
        app.group.create(Group(name="New one", footer="group for test"))
        app.navigation.return_to_homepage()
    if app.group.count_contact_in_group(group_name="New one") == 0:
        app.group.show_all_contacts()
        app.contact.add_first_contact_to_group(group_name="New one")
    app.contact.remove_first_contact_from_group(group_name="New one")
