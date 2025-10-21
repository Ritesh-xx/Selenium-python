from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class CartPage(BasePage):
    """
    Page Object for the Cart Page, focusing on Web Table interaction.
    """
    # Concept 8: Web Tables
    # Locators are structured to find rows (tr) and cells (td) within the table.
    CART_TABLE = (By.ID, "cart_info_table")
    FIRST_ROW_DESCRIPTION = (By.XPATH, "//table[@id='cart_info_table']/tbody/tr[1]/td[@class='cart_description']/h4/a")
    FIRST_ROW_PRICE = (By.XPATH, "//table[@id='cart_info_table']/tbody/tr[1]/td[@class='cart_price']/p")
    FIRST_ROW_QUANTITY = (By.XPATH, "//table[@id='cart_info_table']/tbody/tr[1]/td[@class='cart_quantity']/button")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Verify the cart table is visible")
    def is_cart_table_visible(self):
        """Checks if the main cart table element is displayed."""
        return self.is_element_visible(self.CART_TABLE)

    @allure.step("Get the description from the first row of the cart table")
    def get_first_row_description(self):
        """Reads and returns text from a specific cell in the table."""
        return self.get_element_text(self.FIRST_ROW_DESCRIPTION)

    @allure.step("Get the price from the first row of the cart table")
    def get_first_row_price(self):
        """Reads and returns text from another cell in the table."""
        return self.get_element_text(self.FIRST_ROW_PRICE)