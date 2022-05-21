# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ' '*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_numbers(prefix, maxlen):
    symbols = '+' + string.digits
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(name=random_string('name', 5), surname=random_string('surname', 10),
                    comp_address=random_string('address', 10), comp_name=random_string('com_name', 7),
                    email1=random_string('email', 7), email2=random_string('email2', 7),
                    home_number=random_numbers('home', 11), work_number=random_numbers('work', 11))
            for i in range(2)]


@pytest.mark.parametrize('contact', testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert (len(old_contacts) + 1) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
