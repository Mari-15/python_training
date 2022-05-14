from model.contact import Contact


def test_modify_other_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Roland", surname="Braund"))
        app.contact.create(Contact(name="Voland", surname="Round"))
    old_contacts = app.contact.get_contact_list()
    app.modify.other_contacts(Contact(number_of_contact=2, name="ProstoNewGuy", surname="Robson",
                                      nick="VasiliiParovoz", title="Vasilii Parovoz",
                                      comp_name="OOO \"GoodPeopleComp\"", comp_address="Planate Mars",
                                      work_number="", fax="Yes",
                                      email1="t@mail.ru", day_Birth="1"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
