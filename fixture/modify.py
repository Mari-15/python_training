from selenium.webdriver.common.by import By


class ModifyHelper:

    def __init__(self, app):
        self.app = app

    def first_contact(self, contact):
        wd = self.app.wd
        # init edit first contact
        wd.find_element(by=By.XPATH, value="//img[@alt='Edit']").click()
        self.app.contact.contact_fill_form(contact)
        # submit edit a contact
        wd.find_element(by=By.XPATH, value="//div[@id='content']/form/input[22]").click()
        self.app.navigation.return_to_homepage()

    def other_contacts(self, contact):
        wd = self.app.wd
        # init edit a contact, where tr[3] is a position of contact +1 (№1 = 2, №2 = 3, etc)
        wd.find_element(by=By.XPATH,
                        value=("//table[@id='maintable']/tbody/tr[%s]/td[8]/a/img" % contact.number_of_contact)).click()
        self.app.contact.contact_fill_form(contact)
        # submit edit a contact
        wd.find_element(by=By.XPATH, value="//div[@id='content']/form/input[22]").click()
        self.app.navigation.return_to_homepage()

    def group(self, group):
        wd = self.app.wd
        self.app.group.open_groups_page()
        # init edit group, where span[1] is a number of a group
        wd.find_element(by=By.XPATH,
                        value=("//div[@id='content']/form/span[%s]/input" % group.number_of_group)).click()
        wd.find_element(by=By.NAME, value="edit").click()
        self.app.group.group_fill_form(group)
        # submit edit group
        wd.find_element(by=By.NAME, value="update").click()
        self.app.group.return_to_groups_page()
