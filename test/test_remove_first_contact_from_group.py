from model.contact import Contact
from model.group import Group


def test_remove_first_contact_from_group(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Roland", surname="Braund"))
    name = Group(name="Lol1")
    groups = app.group.get_group_list()
    if name not in groups:
        app.group.create(Group(name=name.name))
    if app.group.count_contact_in_group(group_name=name.name) == 0:
        app.group.show_all_contacts()
        app.contact.add_first_contact_to_group(group_name=name.name)
    app.contact.remove_first_contact_from_group(group_name=name.name)
