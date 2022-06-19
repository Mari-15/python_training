import random
from model.contact import Contact


def test_modify_some_contacts(app, data_contact, db, check_ui):
    contact = data_contact
    if len(db.get_contact_list()) <= 1:
        app.contact.create(contact)
        app.contact.create(contact)
    old_contacts = db.get_contact_list()
    contact1 = random.choice(old_contacts)
    app.modify.contact_by_id(contact1.number_of_contact, contact)
    for i in range(len(old_contacts)):
        if old_contacts[i].number_of_contact == contact1.number_of_contact:
            old_contacts[i] = contact1
        return old_contacts
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
