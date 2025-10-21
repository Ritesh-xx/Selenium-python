from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class ProductsPage(BasePage):
    """Page Object for the Products Page."""

    # Locators
    FIRST_PRODUCT_OVERLAY = (By.CSS_SELECTOR, "div.product-overlay")
    ADD_TO_CART_BUTTON = (By.XPATH, "(//a[@data-product-id='1'])[1]")
    VIEW_CART_LINK = (By.XPATH, "//u[text()='View Cart']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Add the first product to the cart")
    def add_first_product_to_cart(self):
        """
        This method demonstrates:
        - Concept 4: WebElement Methods (move_to_element, click)
        - It uses ActionChains to hover over the product before clicking 'Add to cart'.
        """
        self.move_to_element(self.FIRST_PRODUCT_OVERLAY)
        self.click(self.ADD_TO_CART_BUTTON)

    @allure.step("Click the 'View Cart' link in the modal")
    def click_view_cart(self):
        """Clicks the link to view the cart after adding an item."""
        self.click(self.VIEW_CART_LINK)