import random
from model.contact import Contact


def test_modify_some_contacts(app, data_contact, db, check_ui):
    contact = data_contact
    if len(db.get_contact_list()) <= 1:
        app.contact.create(contact)
        app.contact.create(contact)
    def clean(contact):
        return Contact(number_of_contact=contact.number_of_contact,
                       name=contact.name.strip(), surname=contact.surname.strip())
    old_contacts = db.get_contact_list()
    contact1 = random.choice(old_contacts)
    app.modify.contact_by_id(contact1.number_of_contact, contact)
    new_contacts = db.get_contact_list()
    for i in range(len(old_contacts)):
        if old_contacts[i].number_of_contact == contact1.number_of_contact:
            old_contacts[i] = contact
            old_contacts[i].number_of_contact = contact1.number_of_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        new_contacts = map(clean, db.get_contact_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
