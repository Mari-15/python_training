from model.contact import Contact


def test_modify_first_contact(app, data_contact):
    contact = data_contact
    if app.contact.count() == 0:
        app.contact.create(contact)
    old_contacts = app.contact.get_contact_list()
    contact.number_of_contact = old_contacts[0].number_of_contact
    app.modify.first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
