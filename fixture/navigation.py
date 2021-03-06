from selenium.webdriver.common.by import By


class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url)

    def return_to_homepage(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook"):
            wd.find_element(by=By.LINK_TEXT, value="home").click()
