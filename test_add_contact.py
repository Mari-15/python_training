# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_new_contact(wd, Contact(name="Vasilii", patronymic="Petrovich", surname="Petrov",
                                           nick="VasiliiParovoz", title="Vasilii Parovoz",
                                           comp_name="OOO \"GoodPeopleComp\"", comp_address="The USA, Green str, apt 654",
                                           home_number="8-800-999-45-45", mobile_number="+7(921)456-45-45",
                                           work_number="8-800-555-55-55", fax="No",
                                           email1="testVasili@mail.ru", email2="testVasili2@mail.com",
                                           day_Birth="15", month_Birth="June", year_Birth="1975"))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element(by=By.LINK_TEXT, value="Logout").click()

    def return_to_homepage(self, wd):
        wd.find_element(by=By.LINK_TEXT, value="home").click()

    def create_new_contact(self, wd, contact):
        # init create new contact
        wd.find_element(by=By.LINK_TEXT, value="add new").click()
        # fill contact form
        wd.find_element(by=By.NAME, value="firstname").clear()
        wd.find_element(by=By.NAME, value="firstname").send_keys(contact.name)
        wd.find_element(by=By.NAME, value="middlename").click()
        wd.find_element(by=By.NAME, value="middlename").clear()
        wd.find_element(by=By.NAME, value="middlename").send_keys(contact.patronymic)
        wd.find_element(by=By.NAME, value="lastname").click()
        wd.find_element(by=By.NAME, value="lastname").clear()
        wd.find_element(by=By.NAME, value="lastname").send_keys(contact.surname)
        wd.find_element(by=By.NAME, value="nickname").click()
        wd.find_element(by=By.NAME, value="nickname").clear()
        wd.find_element(by=By.NAME, value="nickname").send_keys(contact.nick)
        wd.find_element(by=By.NAME, value="title").click()
        wd.find_element(by=By.NAME, value="title").clear()
        wd.find_element(by=By.NAME, value="title").send_keys(contact.title)
        wd.find_element(by=By.NAME, value="company").click()
        wd.find_element(by=By.NAME, value="company").clear()
        wd.find_element(by=By.NAME, value="company").send_keys(contact.comp_name)
        wd.find_element(by=By.NAME, value="address").click()
        wd.find_element(by=By.NAME, value="address").clear()
        wd.find_element(by=By.NAME, value="address").send_keys(contact.comp_address)
        wd.find_element(by=By.NAME, value="home").click()
        wd.find_element(by=By.NAME, value="home").clear()
        wd.find_element(by=By.NAME, value="home").send_keys(contact.home_number)
        wd.find_element(by=By.NAME, value="mobile").click()
        wd.find_element(by=By.NAME, value="mobile").clear()
        wd.find_element(by=By.NAME, value="mobile").send_keys(contact.mobile_number)
        wd.find_element(by=By.NAME, value="work").click()
        wd.find_element(by=By.NAME, value="work").clear()
        wd.find_element(by=By.NAME, value="work").send_keys(contact.work_number)
        wd.find_element(by=By.NAME, value="fax").click()
        wd.find_element(by=By.NAME, value="fax").clear()
        wd.find_element(by=By.NAME, value="fax").send_keys(contact.fax)
        wd.find_element(by=By.NAME, value="email").click()
        wd.find_element(by=By.NAME, value="email").clear()
        wd.find_element(by=By.NAME, value="email").send_keys(contact.email1)
        wd.find_element(by=By.NAME, value="email2").click()
        wd.find_element(by=By.NAME, value="email2").clear()
        wd.find_element(by=By.NAME, value="email2").send_keys(contact.email2)
        # select birthdate
        wd.find_element(by=By.NAME, value="bday").click()
        Select(wd.find_element(by=By.NAME, value="bday")).select_by_visible_text(contact.day_Birth)
        wd.find_element(by=By.NAME, value="bmonth").click()
        Select(wd.find_element(by=By.NAME, value="bmonth")).select_by_visible_text(contact.month_Birth)
        wd.find_element(by=By.NAME, value="byear").click()
        wd.find_element(by=By.NAME, value="byear").clear()
        wd.find_element(by=By.NAME, value="byear").send_keys(contact.year_Birth)
        # submit creation new contact
        wd.find_element(by=By.NAME, value="theform").click()
        wd.find_element(by=By.XPATH, value="//div[@id='content']/form/input[21]").click()
        self.return_to_homepage(wd)

    def login(self, wd, username, password):
        self.homepage(wd)
        wd.find_element(by=By.NAME, value="user").click()
        wd.find_element(by=By.NAME, value="user").clear()
        wd.find_element(by=By.NAME, value="user").send_keys(username)
        wd.find_element(by=By.NAME, value="pass").click()
        wd.find_element(by=By.NAME, value="pass").clear()
        wd.find_element(by=By.NAME, value="pass").send_keys(password)
        wd.find_element(by=By.XPATH, value="//input[@value='Login']").click()

    def homepage(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
