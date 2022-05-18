from model.contact import Contact
from random import randrange


def test_modify_some_contacts(app):
    if app.contact.count() == 1:
        app.contact.create(Contact(name="Second", surname="Black"))
        app.contact.create(Contact(name="Third", surname="Jinjer"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(name="Vosr", surname="Rosl")
    contact.number_of_contact = old_contacts[index].number_of_contact
    app.modify.contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
