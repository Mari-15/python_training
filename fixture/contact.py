from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def contact_fill_form(self, contact):
        wd = self.app.wd
        # fill contact form
        self.change_field_value_c("firstname", contact.name)
        self.change_field_value_c("middlename", contact.patronymic)
        self.change_field_value_c("lastname", contact.surname)
        self.change_field_value_c("nickname", contact.nick)
        self.change_field_value_c("title", contact.title)
        self.change_field_value_c("company", contact.comp_name)
        self.change_field_value_c("address", contact.comp_address)
        self.change_field_value_c("home", contact.home_number)
        self.change_field_value_c("mobile", contact.mobile_number)
        self.change_field_value_c("work", contact.work_number)
        self.change_field_value_c("fax", contact.fax)
        self.change_field_value_c("email", contact.email1)
        self.change_field_value_c("email2", contact.email2)
        # select birthdate
        self.change_date_birth("bday", contact.day_Birth)
        self.change_date_birth("bmonth", contact.month_Birth)
        self.change_field_value_c("byear", contact.year_Birth)

    def change_date_birth(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(by=By.NAME, value=field_name).click()
            Select(wd.find_element(by=By.NAME, value=field_name)).select_by_visible_text(text)

    def change_field_value_c(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(by=By.NAME, value=field_name).click()
            wd.find_element(by=By.NAME, value=field_name).clear()
            wd.find_element(by=By.NAME, value=field_name).send_keys(text)

    def create(self, contact):
        wd = self.app.wd
        # init create new contact
        wd.find_element(by=By.LINK_TEXT, value="add new").click()
        self.contact_fill_form(contact)
        # submit creation new contact
        wd.find_element(by=By.NAME, value="theform").click()
        wd.find_element(by=By.XPATH, value="//div[@id='content']/form/input[21]").click()
        self.app.navigation.return_to_homepage()

    def add_first_contact_to_group(self, group_name):
        wd = self.app.wd
        self.select_first_contact()
        self.app.group.open_group_list_and_select_group(group_name)
        # submit add
        wd.find_element(by=By.NAME, value="add").click()
        self.app.navigation.return_to_homepage()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(by=By.NAME, value="selected[]").click()

    def add_all_contacts_to_group(self, group_name):
        wd = self.app.wd
        # select all contacts
        wd.find_element(By.ID, "MassCB").click()
        self.app.group.open_group_list_and_select_group(group_name)
        # submit add
        wd.find_element(by=By.NAME, value="add").click()

    def remove_first_contact_from_group(self, group_name):
        wd = self.app.wd
        # select group
        wd.find_element(by=By.NAME, value="group").click()
        Select(wd.find_element(by=By.NAME, value="group")).select_by_visible_text(group_name)
        self.select_first_contact()
        # submit remove
        wd.find_element(by=By.NAME, value="remove").click()
        self.app.navigation.return_to_homepage()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements(By.NAME, "selected[]"))
