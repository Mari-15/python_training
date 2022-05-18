from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Roland", surname="Braund"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="Anton", surname="Postr", nick="VasiliiParovoz", title="Vasilii Parovoz",
                                     comp_name='OOO "GoodPeopleComp"', comp_address="The USA, Green str, apt 654",
                                     home_number="8-800-999-45-45", mobile_number="+7(921)456-45-45",
                                     fax="Yes", email1="testVasili@mail.ru", day_Birth="15", month_Birth="June",
                                     year_Birth="1975")
    contact.number_of_contact = old_contacts[0].number_of_contact
    app.modify.first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
