from selenium.webdriver.common.by import By


class DeleteHelper:

    def __init__(self, app):
        self.app = app

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element(by=By.NAME, value="selected[]").click()
        # submit deletion
        wd.find_element(by=By.XPATH, value="//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def delete_all_contacts(self):
        wd = self.app.wd
        # select all contacts
        wd.find_element(by=By.ID, value="MassCB").click()
        # submit deletion
        wd.find_element(by=By.XPATH, value="//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
