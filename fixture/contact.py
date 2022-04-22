from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
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
        self.app.navigation.return_to_homepage()