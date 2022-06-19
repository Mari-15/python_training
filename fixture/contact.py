from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


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
        self.change_field_value_c("phone2", contact.phone2)
        self.change_field_value_c("email", contact.email1)
        self.change_field_value_c("email2", contact.email2)
        self.change_field_value_c("email3", contact.email3)
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
        self.contact_cache = None

    def add_some_contact_to_group(self, group_name, id1):
        wd = self.app.wd
        self.select_contact_by_id1(id1)
        self.app.group.open_group_list_and_select_group(group_name)
        # submit add
        wd.find_element(by=By.NAME, value="add").click()
        self.app.navigation.return_to_homepage()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(by=By.NAME, value="selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.CSS_SELECTOR, 'img[alt="Edit"]')[index].click()

    def select_contact_by_id1(self, id1):
        wd = self.app.wd
        wd.find_element(by=By.CSS_SELECTOR, value='[href="edit.php?id=%s"]' % id1).click()

    def add_all_contacts_to_group(self, group_name):
        wd = self.app.wd
        # select all contacts
        wd.find_element(By.ID, "MassCB").click()
        self.app.group.open_group_list_and_select_group(group_name)
        # submit add
        wd.find_element(by=By.NAME, value="add").click()

    def remove_first_contact_from_group(self, group_name, id1):
        wd = self.app.wd
        # select group
        wd.find_element(by=By.NAME, value="group").click()
        Select(wd.find_element(by=By.NAME, value="group")).select_by_visible_text(group_name)
        self.select_contact_by_id1(id1)
        # submit remove
        wd.find_element(by=By.NAME, value="remove").click()
        self.app.navigation.return_to_homepage()

    def count(self):
        wd = self.app.wd
        self.app.navigation.return_to_homepage()
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.navigation.return_to_homepage()
            self.contact_cache = []
            for element in wd.find_elements(by=By.NAME, value="entry"):
                cell = element.find_elements(By.TAG_NAME, 'td')
                surname1 = element.find_element(by=By.CSS_SELECTOR, value="td:nth-child(2)").text
                name1 = element.find_element(by=By.CSS_SELECTOR, value="td:nth-child(3)").text
                id = element.find_element(by=By.NAME, value="selected[]").get_attribute("value")
                all_phones = cell[5].text
                emails = cell[4].text
                homeadress = cell[3].text
                self.contact_cache.append(Contact(number_of_contact=id, surname=surname1, name=name1,
                                                  all_phones_from_homepage=all_phones, all_emails=emails,
                                                  comp_address=homeadress))
        return list(self.contact_cache)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.return_to_homepage()
        row = wd.find_elements(By.NAME, 'entry')[index]
        cell = row.find_elements(By.TAG_NAME, 'td')[6]
        cell.find_element(by=By.TAG_NAME, value='a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.app.navigation.return_to_homepage()
        self.select_contact_by_index(index)
        firstname = wd.find_element(by=By.NAME, value='firstname').get_attribute('value')
        surname = wd.find_element(by=By.NAME, value='lastname').get_attribute('value')
        id = wd.find_element(by=By.NAME, value='id').get_attribute('value')
        homenumber = wd.find_element(by=By.NAME, value='home').get_attribute('value')
        mobilenumber = wd.find_element(by=By.NAME, value='mobile').get_attribute('value')
        worknumber = wd.find_element(by=By.NAME, value='work').get_attribute('value')
        email1 = wd.find_element(by=By.NAME, value='email').get_attribute('value')
        email2 = wd.find_element(by=By.NAME, value='email2').get_attribute('value')
        email3 = wd.find_element(by=By.NAME, value='email3').get_attribute('value')
        phone2 = wd.find_element(by=By.NAME, value='phone2').get_attribute('value')
        address = wd.find_element(by=By.NAME, value='address').get_attribute('value')
        return Contact(name=firstname, surname=surname, id=id, home_number=homenumber,
                       mobile_number=mobilenumber, work_number=worknumber, phone2=phone2,
                       email1=email1, email2=email2,
                       email3= email3, comp_address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(by=By.ID, value='content').text
        if re.search('H:', text) is not None:
            homenumber = re.search('H: (.*)', text).group(1)
        else:
            homenumber = ''
        if re.search('M:', text) is not None:
            mobilenumber = re.search('M: (.*)', text).group(1)
        else:
            mobilenumber = ''
        if re.search('W: (.*)', text) is not None:
            worknumber = re.search('W: (.*)', text).group(1)
        else:
            worknumber = ''
        if re.search('P: (.*)', text) is not None:
            phone2 = re.search('P: (.*)', text).group(1)
        else:
            phone2 = ''
        return Contact(home_number=homenumber, mobile_number=mobilenumber, work_number=worknumber, phone2=phone2)




