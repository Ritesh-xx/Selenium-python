from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
import time

class HomePage(BasePage):
    search_input = (By.ID, "search_product")
    search_button = (By.ID, "submit_search")
    logged_in_user = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a')
    PRODUCTS_BUTTON = (By.CSS_SELECTOR, "a[href='/products']")
    ALL_PRODUCTS = (By.CSS_SELECTOR, ".features_items .product-image-wrapper")


    def search_product(self, product_name):
        self.enter_text(self.search_input, product_name)
        self.click(self.search_button)

    def is_user_logged_in(self):
        return self.is_element_present(self.logged_in_user)
    
    def click_products(self):
        self.click(self.PRODUCTS_BUTTON)

    def scroll_page_down(self, pixels=500):
        """Scrolls the page down by a specified number of pixels."""
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")
        # Adding a pause to visualize the scroll
        time.sleep(1)

    def hover_over_all_products(self):
        """Finds all product items and hovers over each one."""
        product_elements = self.wait_for_all_elements(self.ALL_PRODUCTS)
        print(f"Found {len(product_elements)} products to hover over.")
        
        for i, product in enumerate(product_elements):
            try:
                # We use execute_script to scroll the element into view first
                self.driver.execute_script("arguments[0].scrollIntoView(true);", product)
                # Then use ActionChains to hover
                actions = ActionChains(self.driver)
                actions.move_to_element(product).perform()
                print(f"Hovering over product {i+1}")
                time.sleep(0.5) # Pause to visualize
            except Exception as e:
                print(f"Could not hover over product {i+1}: {e}")