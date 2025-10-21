import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utilities.config import Config

config = Config()

@pytest.mark.usefixtures("setup")
@pytest.mark.parametrize("email,password", [
    (config.get("LOGIN", "email"), config.get("LOGIN", "password")),
    ("invalid@example.com", "wrongpass")
])
class TestLoginLogout:
    def test_login_logout(self, email, password):
        driver = self.driver  # driver injected by setup fixture
        driver.get("https://www.automationexercise.com/")

        login_page = LoginPage(driver)
        login_page.go_to_login_page()
        login_page.login(email, password)

        home_page = HomePage(driver)

        if "invalid" in email:
            assert login_page.is_login_error_displayed()
        else:
            assert home_page.is_user_logged_in()
            login_page.logout()
