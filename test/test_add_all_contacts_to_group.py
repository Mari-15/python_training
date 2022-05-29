from model.contact import Contact
import random


def test_add_all_contacts_to_group(app, db):
    if len(db.get_contact_list()) <= 1:
        app.contact.create(Contact(name="Roland", surname="Braund"))
        app.contact.create(Contact(name="Voland", surname="Round"))
    groups = db.get_group_list()
    group = random.choice(groups)
    app.navigation.return_to_homepage()
    app.contact.add_all_contacts_to_group(group_name=group.name)

