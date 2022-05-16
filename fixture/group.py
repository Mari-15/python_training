from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(By.NAME, "new")) > 0):
            wd.find_element(by=By.LINK_TEXT, value="groups").click()

    def fill_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(by=By.NAME, value=field_name).click()
            wd.find_element(by=By.NAME, value=field_name).clear()
            wd.find_element(by=By.NAME, value=field_name).send_keys(text)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element(by=By.NAME, value="new").click()
        self.fill_form(group)
        # submit group creation
        wd.find_element(by=By.NAME, value="submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(by=By.LINK_TEXT, value="group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def open_group_list_and_select_group(self, group_name):
        wd = self.app.wd
        wd.find_element(by=By.NAME, value="to_group").click()
        Select(wd.find_element(by=By.NAME, value="to_group")).select_by_visible_text(group_name)

    def count_contact_in_group(self, group_name):
        wd = self.app.wd
        self.app.navigation.return_to_homepage()
        wd.find_element(by=By.NAME, value="group").click()
        Select(wd.find_element(by=By.NAME, value="group")).select_by_visible_text(group_name)
        return len(wd.find_elements(By.NAME, "selected[]"))

    def show_all_contacts(self):
        wd = self.app.wd
        wd.find_element(by=By.NAME, value="group").click()
        Select(wd.find_element(by=By.NAME, value="group")).select_by_visible_text("[none]")

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(by=By.NAME, value="selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, value="span.group"):
                text = element.text
                id = element.find_element(by=By.NAME, value="selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)


