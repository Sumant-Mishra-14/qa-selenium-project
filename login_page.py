from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    # Locators
    username = (By.ID, "username")
    password = (By.ID, "password")
    login_button = (By.ID, "login")

    # URL
    url = "https://example.com/login"

    def open_login_page(self):
        self.driver.get(self.url)

    def login(self, user, pwd):
        self.enter_text(self.username, user)
        self.enter_text(self.password, pwd)
        self.click(self.login_button)