import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.base_page import BasePage
import allure, os

from utilities.test_data_reader import read_login_data_from_csv 

# Load only the top 1 user's data from the CSV
login_data = read_login_data_from_csv("utilities/test_data.csv")[:1]

@pytest.mark.usefixtures("setup")
class TestUserInteractions:

    @allure.title("Test Login, Scroll, Hover, and Screenshot Functionality")
    @pytest.mark.parametrize("email,password", login_data)
    def test_login_scroll_hover_screenshot(self, email, password):
        """
        Test flow:
        1. Take screenshot of login page
        2. Read user data from CSV (via parameterization)
        3. Perform login
        4. Take screenshot of home page
        5. Verify login was successful
        6. Scroll down the home page
        7. Hover over all products
        """
        
        # 1. Get driver from conftest setup (using your TestLoginLogout style)
        driver = self.driver 
        
        # 2. Initialize Page Objects
        login_page = LoginPage(driver)
        home_page = HomePage(driver)

        with allure.step("Starting login and interaction test"):
            # 3. Open login page and take screenshot
            login_page.go_to_login_page() # Using the method from your example
            login_page.take_screenshot("login_page_before_login")
        
        # 4. Perform login (using data from @pytest.mark.parametrize)
        # Using the 'login' method name from your TestLoginLogout example
            login_page.login(email, password) 

        with allure.step("Post-login and taking screenshot"):
            # 5. Verify login and take screenshot
            # Using the 'is_user_logged_in' from your TestLoginLogout example
            if home_page.is_user_logged_in():
                home_page.take_screenshot("home_page_after_login")
                assert True
            else:
                home_page.take_screenshot("login_failed")
                assert False, f"Login failed for user {email}."

        with allure.step("Scrolling products"):    
            # 6. Scroll down the page
            home_page.scroll_page_down(pixels=1000)
            
        with allure.step("Hovering over products"):
            # 7. Hover over all products
            home_page.hover_over_all_products()

