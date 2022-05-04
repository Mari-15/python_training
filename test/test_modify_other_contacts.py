import pytest
from model.contact import Contact


def test_modify_other_contacts(app):
    #pytest.skip()
    app.modify.other_contacts(Contact(number_of_contact=2, name="ProstoNewGuy", surname="Robson",
                                      nick="VasiliiParovoz", title="Vasilii Parovoz",
                                      comp_name="OOO \"GoodPeopleComp\"", comp_address="Planate Mars",
                                      work_number="", fax="Yes",
                                      email1="t@mail.ru", day_Birth="1"))
