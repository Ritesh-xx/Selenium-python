from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.wait_utils import WaitUtils

class CustomerPage(BasePage):
    
    SIGNUP_LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")
    SIGNUP_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    SIGNUP_EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")

    # --- Locators for the 'ENTER ACCOUNT INFORMATION' section ---
    TITLE_MR_RADIO = (By.ID, "id_gender1")
    PASSWORD_INPUT = (By.ID, "password")
    DOB_DAY_DROPDOWN = (By.ID, "days")
    DOB_MONTH_DROPDOWN = (By.ID, "months")
    DOB_YEAR_DROPDOWN = (By.ID, "years")
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    SPECIAL_OFFERS_CHECKBOX = (By.ID, "optin")
    
    # --- Locators for the 'ADDRESS INFORMATION' section ---
    FIRST_NAME_INPUT = (By.ID, "first_name")
    LAST_NAME_INPUT = (By.ID, "last_name")
    ADDRESS_INPUT = (By.ID, "address1")
    COUNTRY_DROPDOWN = (By.ID, "country")
    STATE_INPUT = (By.ID, "state")
    CITY_INPUT = (By.ID, "city")
    ZIPCODE_INPUT = (By.ID, "zipcode")
    MOBILE_NUMBER_INPUT = (By.ID, "mobile_number")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//*[@id='form']/div/div/div/div[1]/form/button")
    ACCOUNT_CREATED_TEXT = (By.XPATH, "//b[normalize-space()='Account Created!']")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='form']/div/div/div/h2/b")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[data-qa='continue-button']")
    # SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#success_message")
    
    def __init__(self, driver):
        super().__init__(driver)

    # --- Your requested functions, modified to use BasePage ---

    @allure.step("Navigate to the Signup / Login page")
    def go_to_signup_page(self):
        """Clicks the 'Signup / Login' link from the homepage."""
        self.click(self.SIGNUP_LOGIN_LINK)

    @allure.step("Start new customer signup with name and email")
    def signup_new_customer(self, name, email):
        """Enters name and email on the login page and clicks 'Signup'."""
        self.enter_text(self.SIGNUP_NAME_INPUT, name)
        self.enter_text(self.SIGNUP_EMAIL_INPUT, email)
        self.click(self.SIGNUP_BUTTON)
        
    # --- Action methods for the detailed form ---

    @allure.step("Filling out the customer details form")
    def fill_customer_details(self, user_data):
        """
        Fills the entire detailed customer registration form.
        'user_data' is expected to be a dictionary-like object.
        """
        self.click(self.TITLE_MR_RADIO)
        self.enter_text(self.PASSWORD_INPUT, user_data['password'])
        
        Select(self.wait_for_element(self.DOB_DAY_DROPDOWN)).select_by_visible_text(str(user_data['dob_day']))
        Select(self.wait_for_element(self.DOB_MONTH_DROPDOWN)).select_by_visible_text(user_data['dob_month'])
        Select(self.wait_for_element(self.DOB_YEAR_DROPDOWN)).select_by_visible_text(str(user_data['dob_year']))
        
        self.click(self.NEWSLETTER_CHECKBOX)
        self.click(self.SPECIAL_OFFERS_CHECKBOX)

        self.enter_text(self.FIRST_NAME_INPUT, user_data['first_name'])
        self.enter_text(self.LAST_NAME_INPUT, user_data['last_name'])
        self.enter_text(self.ADDRESS_INPUT, user_data['address'])
        Select(self.wait_for_element(self.COUNTRY_DROPDOWN)).select_by_visible_text(user_data['country'])
        self.enter_text(self.STATE_INPUT, user_data['state'])
        self.enter_text(self.CITY_INPUT, user_data['city'])
        self.enter_text(self.ZIPCODE_INPUT, str(user_data['zipcode']))
        self.enter_text(self.MOBILE_NUMBER_INPUT, str(user_data['mobile']))

    @allure.step("Submitting the new account form")
    def submit_creation_form(self):
        self.wait_for_element(self.CREATE_ACCOUNT_BUTTON)
        self.js_click(self.CREATE_ACCOUNT_BUTTON)

    @allure.step("Verifying the 'Account Created!' success message")
    def is_account_created_message_visible(self):
        """Checks if the account creation success message is displayed."""
        return self.is_element_visible(self.ACCOUNT_CREATED_TEXT)
    
    @allure.step("Selecting day from Date of Birth dropdown")
    def select_day_from_dropdown(self, day):
        dropdown = Select(self.driver.find_element(*self.DOB_DAY_DROPDOWN))
        dropdown.select_by_visible_text(day)

    @allure.step("Selecting month from Date of Birth dropdown")
    def select_month_from_dropdown(self, month):
        dropdown = Select(self.driver.find_element(*self.DOB_MONTH_DROPDOWN))
        dropdown.select_by_visible_text(month)

    @allure.step("Selecting year from Date of Birth dropdown")
    def select_year_from_dropdown(self, year):
        dropdown = Select(self.driver.find_element(*self.DOB_YEAR_DROPDOWN))
        dropdown.select_by_visible_text(str(year))

    @allure.step("Getting the success message text")
    def get_success_message(self):
        element = self.wait_for_element(self.SUCCESS_MESSAGE)
        return element.text