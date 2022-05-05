from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Roland", surname="Braund"))
    app.modify.first_contact(Contact(name="Anton", nick="VasiliiParovoz", title="Vasilii Parovoz",
                                     comp_name="OOO \"GoodPeopleComp\"", comp_address="The USA, Green str, apt 654",
                                     home_number="8-800-999-45-45", mobile_number="+7(921)456-45-45",
                                     fax="Yes", email1="testVasili@mail.ru", day_Birth="15", month_Birth="June",
                                     year_Birth="1975"))
