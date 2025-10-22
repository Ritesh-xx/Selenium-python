# THIS IS POM MODEL
# this is main file for pages object model

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click(self, locator):
        """Waits for an element to be clickable and then performs a standard click."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        """Waits for an element to be visible, clears it, and enters text."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Waits for an element to be visible and returns its text."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_element_present(self, locator):
        """Checks if an element is present in the DOM."""
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException: # Corrected the exception type for clarity
            return False
     
    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def js_click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def take_screenshot(self, file_path):
        """Saves a screenshot of the current page."""
        self.driver.save_screenshot(file_path)

    def move_to_element(self, locator):
        """Performs a mouse hover action on an element."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def scroll_to(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

    def is_element_visible(self, locator, timeout=10):
        """
        Returns True if the element located by the given locator is visible within the timeout.
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    