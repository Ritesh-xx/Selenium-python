from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    search_input = (By.ID, "search_product")
    search_button = (By.ID, "submit_search")
    logged_in_user = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a')
    PRODUCTS_BUTTON = (By.CSS_SELECTOR, "a[href='/products']")


    def search_product(self, product_name):
        self.enter_text(self.search_input, product_name)
        self.click(self.search_button)

    def is_user_logged_in(self):
        return self.is_element_present(self.logged_in_user)
    
    def click_products(self):
        self.click(self.PRODUCTS_BUTTON)
