import pytest
from pages.home_page import HomePage

@pytest.mark.usefixtures("setup")
@pytest.mark.parametrize("product_name", [
    "Dress",
    "Tshirt",
    "Jeans"
])
class TestSearchProduct:
    def test_search_product(self, product_name):
        driver = self.driver  # injected driver from setup fixture
        driver.get("https://www.automationexercise.com/products")

        home_page = HomePage(driver)
        home_page.search_product(product_name)

        # Add assertion for search results as per site behavior, e.g.:
        assert product_name.lower() in driver.page_source.lower()

