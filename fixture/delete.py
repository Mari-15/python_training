from selenium.webdriver.common.by import By


class DeleteHelper:

    def __init__(self, app):
        self.app = app

    def first_contact(self):
        self.contact_by_index(0)

    def contact_by_index(self, index):
        wd = self.app.wd
        self.app.contact.select_contact_by_index(index)
        # submit deletion
        wd.find_element(by=By.XPATH, value="//input[@value='Delete']").click()
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
        self.group_by_index(0)

    def group_by_index(self, index):
        wd = self.app.wd
        self.app.group.open_groups_page()
        self.app.group.select_group_by_index(index)
        # submit deletion
        wd.find_element(by=By.NAME, value="delete").click()
        self.app.group.return_to_groups_page()
        self.app.group.group_cache = None

