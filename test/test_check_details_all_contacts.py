from model.contact import Contact
import re


def test_check_details_all_contacts(app, db, data_contact):
    contact_new = data_contact
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact_new)
    def clean(contact):
        return Contact(number_of_contact=contact.number_of_contact, name=contact.name.strip(),
                       surname=contact.surname.strip(), comp_address=contact.comp_address,
                       email1=contact.email1, email2=contact.email2, email3=contact.email3,
                       home_number=contact.home_number, mobile_number=contact.mobile_number,
                       work_number=contact.work_number, phone2=contact.phone2)
    contact_from_homepage = app.contact.get_contact_list()
    contact_from_db = list(map(clean, db.get_contact_list()))
    for i in range(len(contact_from_homepage)):
        assert contact_from_homepage[i].all_emails == merge_emails_like_on_homepage(contact_from_db[i])
    for i in range(len(contact_from_homepage)):
        assert contact_from_homepage[i].all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_db[i])
    assert sorted(contact_from_homepage, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)


def clear(s):
    return re.sub('[() -]', '', s)


def merge_phones_like_on_homepage(contact):
    return '\n'.join(filter(lambda x: x != '',
                     map(lambda x: clear(x),
                     filter(lambda x: x is not None,
                     [contact.home_number, contact.mobile_number, contact.work_number, contact.phone2]))))


def merge_emails_like_on_homepage(contact):
    return '\n'.join(filter(lambda x: x != '',
                     filter(lambda x: x is not None,
                     [contact.email1, contact.email2, contact.email3])))