from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


class BrowserFactory:
    @staticmethod
    def get_driver(browser_name="chrome", headless=False):
        browser_name = browser_name.lower()
        
        if browser_name == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless")
                options.add_argument("--window-size=1920,1080")
            driver = webdriver.Chrome(options=options)
        
        elif browser_name == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
                options.add_argument("--width=1920")
                options.add_argument("--height=1080")
            driver = webdriver.Firefox(options=options)
        
        elif browser_name == "edge":
            options = EdgeOptions()
            if headless:
                options.add_argument("--headless")
                options.add_argument("--window-size=1920,1080")
            driver = webdriver.Edge(options=options)
        
        else:
            raise Exception(f"Browser '{browser_name}' is not supported.")
        
        if not headless:
            driver.maximize_window()
        
        return driver
