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
        self.app.contact.contact_cache = None

    def contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.contact.select_contact_by_index(index)
        # open modification form
        wd.find_element(by=By.CSS_SELECTOR, value="img[alt=\"Edit\"]").click()
        self.app.contact.contact_fill_form(contact)
        # submit edit a contact
        wd.find_element(by=By.XPATH, value="//div[@id='content']/form/input[22]").click()
        self.app.navigation.return_to_homepage()
        self.app.contact.contact_cache = None

    def group_by_index(self, index, group):
        wd = self.app.wd
        self.app.group.open_groups_page()
        self.app.group.select_group_by_index(index)
        # open modification form
        wd.find_element(by=By.NAME, value="edit").click()
        self.app.group.fill_form(group)
        # submit edit group
        wd.find_element(by=By.NAME, value="update").click()
        self.app.group.return_to_groups_page()
        self.app.group.group_cache = None

    def group(self):
        self.group_by_index(0)
