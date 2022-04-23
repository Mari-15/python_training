from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify(Contact(number_of_contact=None, name="Anton", patronymic="", surname="",
                               nick="VasiliiParovoz", title="Vasilii Parovoz",
                               comp_name="OOO \"GoodPeopleComp\"", comp_address="The USA, Green str, apt 654",
                               home_number="8-800-999-45-45", mobile_number="+7(921)456-45-45",
                               work_number="", fax="Yes",
                               email1="testVasili@mail.ru", email2="",
                               day_Birth="15", month_Birth="June", year_Birth="1975"))
    app.session.logout()
