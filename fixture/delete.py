from selenium.webdriver.common.by import By


class DeleteHelper:

    def __init__(self, app):
        self.app = app

    def first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element(by=By.NAME, value="selected[]").click()
        # submit deletion
        wd.find_element(by=By.XPATH, value="//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.navigation.return_to_homepage()
        self.app.contact.contact_cache = None

    def all_contacts(self):
        wd = self.app.wd
        # select all contacts
        wd.find_element(by=By.ID, value="MassCB").click()
        # submit deletion
        wd.find_element(by=By.XPATH, value="//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.navigation.return_to_homepage()
        self.app.contact.contact_cache = None

    def first_group(self):
        wd = self.app.wd
        self.app.group.open_groups_page()
        # select first group
        wd.find_element(by=By.NAME, value="selected[]").click()
        # submit deletion
        wd.find_element(by=By.NAME, value="delete").click()
        self.app.group.return_to_groups_page()
        self.app.group.group_cache = None

