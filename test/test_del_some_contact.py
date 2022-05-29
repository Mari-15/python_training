from model.contact import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(name="Roland", surname="Braund"))
    def clean(contact):
        return Contact(number_of_contact=contact.number_of_contact,
                       name=contact.name.strip(), surname=contact.surname.strip())
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.delete.contact_by_id1(contact.number_of_contact)
    assert (len(old_contacts) - 1) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        new_contacts = map(clean, db.get_contact_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
