# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application_for_contact import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(name="Vasilii", patronymic="Petrovich", surname="Petrov",
               nick="VasiliiParovoz", title="Vasilii Parovoz",
               comp_name="OOO \"GoodPeopleComp\"", comp_address="The USA, Green str, apt 654",
               home_number="8-800-999-45-45", mobile_number="+7(921)456-45-45",
               work_number="8-800-555-55-55", fax="No",
               email1="testVasili@mail.ru", email2="testVasili2@mail.com",
               day_Birth="15", month_Birth="June", year_Birth="1975"))
    app.logout()