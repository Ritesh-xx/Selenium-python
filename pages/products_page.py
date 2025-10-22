from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class ProductsPage(BasePage):
    """Page Object for the Products Page."""

    # Locators
    FIRST_PRODUCT_OVERLAY = (By.CSS_SELECTOR, "div.product-overlay")
    ADD_TO_CART_BUTTON = (By.XPATH, "(//a[@data-product-id='1'])[1]")
    VIEW_CART_LINK = (By.XPATH, "//u[text()='View Cart']")
    FIRST_PRODUCT_CONTAINER = (By.CSS_SELECTOR, ".col-sm-4 .product-image-wrapper .productinfo")
    FIRST_PRODUCT_ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".product-image-wrapper .productinfo .add-to-cart")
    SUCCESS_MESSAGE = (By.XPATH, "//h2[text()='Added!']")

    def __init__(self, driver):
        super().__init__(driver)
        self.actions = ActionChains(self.driver)



    @allure.step("Click the 'View Cart' link in the modal")
    def click_view_cart(self):
        """Clicks the link to view the cart after adding an item."""
        self.click(self.VIEW_CART_LINK)

    @allure.step("Hover over first product and add to cart")
    def hover_and_add_first_product_to_cart(self):
        wait = WebDriverWait(self.driver, 10)
        product_element = wait.until(
            EC.presence_of_element_located(self.FIRST_PRODUCT_CONTAINER)
        )
        self.actions.move_to_element(product_element).perform()

        add_to_cart_btn = wait.until(
            EC.visibility_of_element_located(self.FIRST_PRODUCT_ADD_TO_CART_BTN)
        )
        # add_to_cart_btn.click()
         # Scroll into view to avoid ads/iframes overlapping
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_cart_btn)

        # Try clicking with JS to bypass overlays
        try:
            add_to_cart_btn.click()
        except Exception as e:
            # If still intercepted, fallback to JS click
            self.driver.execute_script("arguments[0].click();", add_to_cart_btn)
        
    