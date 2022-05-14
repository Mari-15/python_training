# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(name="Vasilii", patronymic="Petrovich", surname="Petrov",
                               nick="VasiliiParovoz",
                               comp_name="OOO \"GoodPeopleComp\"", comp_address="The USA, Green str, apt 654",
                               home_number="8-800-999-45-45", mobile_number="+7(921)456-45-45",
                               work_number="8-800-555-55-55", fax="No",
                               email1="testVasili@mail.ru", email2="testVasili2@mail.com",
                               day_Birth="15", month_Birth="June", year_Birth="1975"))
    new_contacts = app.contact.get_contact_list()
    assert (len(old_contacts) + 1) == len(new_contacts)
