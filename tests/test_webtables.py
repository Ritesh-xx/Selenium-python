import os
import pytest
import allure
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utilities.test_data_reader import read_login_data_from_csv

login_data = read_login_data_from_csv("utilities/test_data.csv")
user = login_data[0]  # get only first user tuple

@pytest.mark.usefixtures("setup")
@allure.feature("Web Tables")
class TestCartWebTable:

    @allure.title("Test Interaction with a Web Table in the Cart")
    @allure.description("This test logs in using credentials from CSV, adds a product to the cart, and verifies its details in the cart's web table.")
    def test_cart_web_table(self):
        login = LoginPage(self.driver)
        home = HomePage(self.driver)
        products = ProductsPage(self.driver)
        cart = CartPage(self.driver)

        email = user[0]
        password = user[1]

        with allure.step(f"Logging in with user: {email}"):
            login.go_to_login_page()
            login.login(email, password)

        with allure.step("Go to products and search for 'jeans'"):
            home.click_products()
            home.search_product("jeans")


        with allure.step("Add first jeans product to cart"):
            products.hover_and_add_first_product_to_cart()

        
        with allure.step("View cart and verify"):
            products.click_view_cart()
            assert cart.is_cart_table_visible(), "Cart's web table should be visible."

            description = cart.get_first_row_description()
            price = cart.get_first_row_price()

            assert "jeans" in description.lower(), "The product description does not contain 'jeans'."

        with allure.step("taking screenshot of cart page"):
            os.makedirs("Reports", exist_ok=True)
            screenshot_path = "Reports/cart_page.png"

            self.driver.save_screenshot(screenshot_path)
            allure.attach.file(
                screenshot_path,
                name="Cart Page Screenshot",
                attachment_type=allure.attachment_type.PNG
            )