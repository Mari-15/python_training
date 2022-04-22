# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_add_group(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.creat_group(wd, Group(name="fgdfgdfgfd", header="dпавпвап", footer="вапвапвапва"))
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.creat_group(wd, Group(name="", header="", footer=""))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element(by=By.LINK_TEXT, value="Logout").click()

    def return_to_groups_page(self, wd):
        wd.find_element(by=By.LINK_TEXT, value="group page").click()

    def creat_group(self, wd, group):
        self.open_groups_page(wd)
        # init group creation
        wd.find_element(by=By.NAME, value="new").click()
        # fill group form
        wd.find_element(by=By.NAME, value="group_name").click()
        wd.find_element(by=By.NAME, value="group_name").clear()
        wd.find_element(by=By.NAME, value="group_name").send_keys(group.name)
        wd.find_element(by=By.NAME, value="group_header").click()
        wd.find_element(by=By.NAME, value="group_header").clear()
        wd.find_element(by=By.NAME, value="group_header").send_keys(group.header)
        wd.find_element(by=By.NAME, value="group_footer").click()
        wd.find_element(by=By.NAME, value="group_footer").clear()
        wd.find_element(by=By.NAME, value="group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element(by=By.NAME, value="submit").click()
        self.return_to_groups_page(wd)

    def open_groups_page(self, wd):
        wd.find_element(by=By.LINK_TEXT, value="groups").click()

    def login(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element(by=By.NAME, value="user").click()
        wd.find_element(by=By.NAME, value="user").clear()
        wd.find_element(by=By.NAME, value="user").send_keys(username)
        wd.find_element(by=By.NAME, value="pass").clear()
        wd.find_element(by=By.NAME, value="pass").send_keys(password)
        wd.find_element(by=By.XPATH, value="//input[@value='Login']").click()

    def open_home_page(self, wd):
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
