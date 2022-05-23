import re
from random import randrange


def test_check_details_some_contact(app, data_contact):
    contact = data_contact
    if app.contact.count() == 0:
        app.contact.create(contact)
    contact = app.contact.get_contact_list()
    index = randrange(len(contact))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)
    assert contact_from_homepage.all_emails == merge_emails_like_on_homepage(contact_from_edit_page)
    assert contact_from_homepage.surname == contact_from_edit_page.surname
    assert contact_from_homepage.name == contact_from_edit_page.name
    assert contact_from_homepage.comp_address == contact_from_edit_page.comp_address


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