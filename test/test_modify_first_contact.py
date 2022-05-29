from model.contact import Contact


def test_modify_first_contact(app, db, data_contact, check_ui):
    contact = data_contact
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact)
    def clean(contact):
        return Contact(number_of_contact=contact.number_of_contact,
                       name=contact.name.strip(), surname=contact.surname.strip())
    old_contacts = db.get_contact_list()
    contact.number_of_contact = old_contacts[0].number_of_contact
    app.modify.first_contact(contact)
    assert len(old_contacts) == len(db.get_contact_list())
    new_contacts = db.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        new_contacts = map(clean, db.get_contact_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
