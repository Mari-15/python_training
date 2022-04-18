# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.homepage(wd)
        self.login(wd)
        self.creat_new_contact(wd)
        self.return_to_homepage(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element(by=By.LINK_TEXT, value="Logout").click()

    def return_to_homepage(self, wd):
        wd.find_element(by=By.LINK_TEXT, value="home").click()

    def creat_new_contact(self, wd):
        # init create new contact
        wd.find_element(by=By.LINK_TEXT, value="add new").click()
        # fill form
        wd.find_element(by=By.NAME, value="firstname").clear()
        wd.find_element(by=By.NAME, value="firstname").send_keys("User_test")
        wd.find_element(by=By.NAME, value="middlename").click()
        wd.find_element(by=By.NAME, value="middlename").clear()
        wd.find_element(by=By.NAME, value="middlename").send_keys("User_testovich")
        wd.find_element(by=By.NAME, value="lastname").click()
        wd.find_element(by=By.NAME, value="lastname").clear()
        wd.find_element(by=By.NAME, value="lastname").send_keys("User_familia")
        wd.find_element(by=By.NAME, value="nickname").click()
        wd.find_element(by=By.NAME, value="nickname").clear()
        wd.find_element(by=By.NAME, value="nickname").send_keys("VasiliiParovoz")
        wd.find_element(by=By.NAME, value="title").click()
        wd.find_element(by=By.NAME, value="title").clear()
        wd.find_element(by=By.NAME, value="title").send_keys("Vasilii Parovoz")
        wd.find_element(by=By.NAME, value="company").click()
        wd.find_element(by=By.NAME, value="company").clear()
        wd.find_element(by=By.NAME, value="company").send_keys("OOO \"GoodPeopleComp\"")
        wd.find_element(by=By.NAME, value="address").click()
        wd.find_element(by=By.NAME, value="address").clear()
        wd.find_element(by=By.NAME, value="address").send_keys("The USA, Green str, apt 654")
        wd.find_element(by=By.NAME, value="home").click()
        wd.find_element(by=By.NAME, value="home").clear()
        wd.find_element(by=By.NAME, value="home").send_keys("8-800-999-45-45")
        wd.find_element(by=By.NAME, value="mobile").click()
        wd.find_element(by=By.NAME, value="mobile").clear()
        wd.find_element(by=By.NAME, value="mobile").send_keys("+7(921)456-45-45")
        wd.find_element(by=By.NAME, value="work").click()
        wd.find_element(by=By.NAME, value="work").clear()
        wd.find_element(by=By.NAME, value="work").send_keys("8-800-555-55-55")
        wd.find_element(by=By.NAME, value="fax").click()
        wd.find_element(by=By.NAME, value="fax").clear()
        wd.find_element(by=By.NAME, value="fax").send_keys("No")
        wd.find_element(by=By.NAME, value="email").click()
        wd.find_element(by=By.NAME, value="email").clear()
        wd.find_element(by=By.NAME, value="email").send_keys("testVasili@mail.ru")
        wd.find_element(by=By.NAME, value="email2").click()
        wd.find_element(by=By.NAME, value="email2").clear()
        wd.find_element(by=By.NAME, value="email2").send_keys("testVasili2@mail.com")
        # select birthdate
        wd.find_element(by=By.NAME, value="bday").click()
        Select(wd.find_element(by=By.NAME, value="bday")).select_by_visible_text("1")
        wd.find_element(by=By.XPATH, value="//option[@value='1']").click()
        wd.find_element(by=By.NAME, value="bmonth").click()
        Select(wd.find_element(by=By.NAME, value="bmonth")).select_by_visible_text("July")
        wd.find_element(by=By.XPATH, value="//option[@value='July']").click()
        wd.find_element(by=By.NAME, value="byear").click()
        wd.find_element(by=By.NAME, value="byear").clear()
        wd.find_element(by=By.NAME, value="byear").send_keys("1968")
        # submit creation new contact
        wd.find_element(by=By.NAME, value="theform").click()
        wd.find_element(by=By.XPATH, value="//div[@id='content']/form/input[21]").click()

    def login(self, wd):
        wd.find_element(by=By.NAME, value="user").click()
        wd.find_element(by=By.NAME, value="user").clear()
        wd.find_element(by=By.NAME, value="user").send_keys("admin")
        wd.find_element(by=By.NAME, value="pass").click()
        wd.find_element(by=By.NAME, value="pass").clear()
        wd.find_element(by=By.NAME, value="pass").send_keys("secret")
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
