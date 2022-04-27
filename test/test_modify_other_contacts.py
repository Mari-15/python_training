import pytest
from model.contact import Contact


def test_modify_other_contacts(app):
    pytest.skip()
    app.session.login(username="admin", password="secret")
    app.modify.other_contacts(Contact(number_of_contact=2, name="Number6", patronymic="", surname="Yaho",
                                      nick="VasiliiParovoz", title="Vasilii Parovoz",
                                      comp_name="OOO \"GoodPeopleComp\"", comp_address="Tt 654",
                                      home_number="", mobile_number="",
                                      work_number="", fax="Yes",
                                      email1="t@mail.ru", email2="",
                                      day_Birth="15", month_Birth="June", year_Birth="1975"))
    app.session.logout()
