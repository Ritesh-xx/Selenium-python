# THIS IS POM MODEL
# this is main file for pages object model

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time
import allure
import os
from datetime import datetime
# from allure_pytest.plugin import AllureImpl
from allure_commons.types import AttachmentType
from selenium.common.exceptions import StaleElementReferenceException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # def click(self, locator):
    #     """Waits for an element to be clickable and then performs a standard click."""
    #     self.wait.until(EC.element_to_be_clickable(locator)).click()

    def click(self, locator, retries=3):
   
        for attempt in range(retries):
            try:
                element = self.wait.until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if attempt == retries - 1:
                    raise
                time.sleep(0.5) 

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

    # def take_screenshot(self, file_path):
    #     """Saves a screenshot of the current page."""
    #     self.driver.save_screenshot(file_path)

    def move_to_element(self, locator):
        """Performs a mouse hover action on an element."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()

    # def scroll_to(self, locator):
    #     element = self.wait.until(EC.presence_of_element_located(locator))
    #     self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

    def scroll_to(self, locator):
        """Waits for element to be visible and scrolls it into the center of the view."""
        try:
            # Wait for the element to be visible
            element = self.wait.until(EC.visibility_of_element_located(locator)) 
            
            # Use JavaScript to scroll the element into view
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        except Exception as e:
            print(f"Error scrolling to element {locator}: {e}")
            # You could add a screenshot here if you want
            # self.take_screenshot(f"scroll_error_{locator}")

    

    def is_element_visible(self, locator, timeout=10):
        """
        Returns True if the element located by the given locator is visible within the timeout.
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    #for ss
    def wait_for_all_elements(self, by_locator):
        """Waits for all elements matching locator to be visible."""
        try:
            return self.wait.until(EC.visibility_of_all_elements_located(by_locator))
        except TimeoutException:
            print(f"Error: No elements found or visible within timeout: {by_locator}")
            self.take_screenshot(f"elements_not_found_{by_locator}")
            return []
        
    def take_screenshot(self, test_name):
        """
        Takes a screenshot with a fixed name (replaces if exists)
        and attaches it to the Allure report.
        """
        # reports folder (same level as your framework root)
        reports_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'reports')
        os.makedirs(reports_dir, exist_ok=True)

        # ✅ fixed filename (no timestamp)
        filename = f"{test_name}.png"
        filepath = os.path.join(reports_dir, filename)

        try:
            # ✅ Overwrite existing file automatically
            self.driver.save_screenshot(filepath)
            print(f"Screenshot saved (replaced if existed): {filepath}")

            # ✅ Attach to Allure
            allure.attach.file(
                filepath,
                name=test_name,
                attachment_type=AttachmentType.PNG
            )

        except Exception as e:
            print(f"Error taking screenshot: {e}")



    # def take_screenshot(self, test_name):
    #     """
    #     Takes a screenshot, saves it, and attaches it to the Allure report.
    #     """
    #     # --- This part is the same as before ---
    #     reports_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'reports')
    #     os.makedirs(reports_dir, exist_ok=True)
        
    #     timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    #     filename = f"{test_name}_{timestamp}.png"
    #     filepath = os.path.join(reports_dir, filename)
        
    #     try:
    #         self.driver.save_screenshot(filepath)
    #         print(f"Screenshot saved: {filepath}")

    #         # --- NEW: Attach to Allure Report ---
    #         allure.attach(
    #             self.driver.get_screenshot_as_png(),
    #             name=test_name,
    #             attachment_type=AttachmentType.PNG
    #         )
    #         # --- End of new code ---

    #     except Exception as e:
    #         print(f"Error taking screenshot: {e}")
     