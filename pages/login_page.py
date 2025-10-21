from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    login_link = (By.XPATH, "//a[contains(text(),'Signup / Login')]")
    email_input = (By.NAME, "email")
    password_input = (By.NAME, "password")
    login_button = (By.XPATH, "//button[contains(text(),'Login')]")
    logout_link = (By.XPATH, "//a[contains(text(),'Logout')]")
    login_error = (By.XPATH, "//p[contains(text(),'Your email or password is incorrect!')]")

    def go_to_login_page(self):
        self.click(self.login_link)

    def login(self, email, password):
        self.enter_text(self.email_input, email)
        self.enter_text(self.password_input, password)
        self.click(self.login_button)

    def logout(self):
        self.click(self.logout_link)

    def is_login_error_displayed(self):
        return self.is_element_present(self.login_error)
