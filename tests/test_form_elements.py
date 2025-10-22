import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.customer_page import CustomerPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from faker import Faker
import allure
from utilities.test_data_writer import write_user_to_csv
 
@pytest.mark.usefixtures("setup")
@allure.epic("UI Element Interactions")
class TestFormElements:

    @allure.feature("Forms")
    @allure.title("Test Interaction with Radio Buttons, Checkboxes, and Dropdowns")
    @allure.description("This test verifies the selection of various form elements on the signup page.")
    def test_signup_form_elements(self):
        # --- Setup ---
        # Initialize all the page objects you will need for the flow
        home = HomePage(self.driver)
        login = LoginPage(self.driver)
        customer = CustomerPage(self.driver)
        fake = Faker()

        # --- Test Steps ---
        # This is a cleaner, more readable flow that follows POM.
        # Each page object is responsible for actions on its own page.
        with allure.step("Navigate to signup page and start registration"):
            customer.go_to_signup_page()
            email = fake.email()
            name = fake.name()
            customer.signup_new_customer(name, email)

        # Now, interact with the elements on the CustomerPage.
        # The test calls high-level methods. The details of finding and clicking
        # are handled inside the CustomerPage object.
        with allure.step("Interact with Radio Button"):
            # Assume CustomerPage has a method 'select_title_mr'
            # that uses self.click(self.TITLE_MR_RADIO)
            customer.js_click(customer.TITLE_MR_RADIO)
            # You would ideally have a method like 'is_title_mr_selected()'
            # in CustomerPage to verify this.

        with allure.step("Interact with Checkbox"):
            customer.js_click(customer.NEWSLETTER_CHECKBOX)
            # You would ideally have a method like 'is_newsletter_checked()'
            # in CustomerPage to verify this.

        with allure.step("Interact with Dropdown"):
            # The logic for selecting from a dropdown is best kept in the page object.
            # Assume CustomerPage has a method 'select_day_of_birth(day)'.
            customer.select_day_from_dropdown("10")
            customer.select_month_from_dropdown("May")
            customer.select_year_from_dropdown("2003")

        with allure.step("address information"):
            user_data = {
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'address': fake.address(),
                'country': "Canada",
                'state': fake.state(),
                'city': fake.city(),
                'zipcode': fake.postcode(),
                'mobile': fake.phone_number(),
                'password': "Test@1234",
                'dob_day': 10,
                'dob_month': "May",
                'dob_year': 2003,
                'email': email 
            }
            customer.fill_customer_details(user_data)
            customer.submit_creation_form()
            write_user_to_csv("utilities/test_data.csv", user_data)

        with allure.step("Submit form and verify account creation by URL"):
            # customer.submit_creation_form()
            current_url = self.driver.current_url
            expected_url_fragment = "account_created"  

            assert expected_url_fragment in current_url, (
                f"Expected URL to contain '{expected_url_fragment}', but got '{current_url}'"
            )
   