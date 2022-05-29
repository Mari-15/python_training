from model.contact import Contact


def test_check_details_all_contacts(app, db, data_contact):
    contact_new = data_contact
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact_new)
    def clean(contact):
        return Contact(number_of_contact=contact.number_of_contact, name=contact.name.strip(),
                       surname=contact.surname.strip(), comp_address=contact.comp_address,
                       all_emails=contact.all_emails,
                       all_phones_from_homepage=contact.all_phones_from_homepage)
    contact_from_homepage = app.contact.get_contact_list()
    contact_from_db = map(clean, db.get_contact_list())
    assert sorted(contact_from_homepage, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)