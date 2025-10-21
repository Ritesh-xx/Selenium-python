# this file is used to define fixtures and hooks for pytest
import pytest
from utilities.browser_factory import BrowserFactory
import configparser  # <--- Step 1: Import the configparser library
import os # <--- Import os to handle file paths reliably

# This new fixture will read the config file ONCE per test session
@pytest.fixture(scope="session")
def config():
    """Reads the config.ini file and returns the config object."""
    config = configparser.ConfigParser()
    # Construct an absolute path to the config.ini file
    config_path = os.path.join(os.path.dirname(__file__), 'utilities', 'config.ini')

     # Add a check to ensure the file is found
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found at: {config_path}")
    
    config.read(config_path)
    return config

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests")
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")

# Update the setup fixture to accept the new 'config' fixture
@pytest.fixture(scope="class")
def setup(request, config): # <--- Step 2: Add 'config' as an argument
    """
    The main setup fixture. It now reads the config, creates the driver,
    and navigates to the base_url before handing control to the test.
    """
    # Get browser settings
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    
    # --- Step 3: Read the base_url from the config object ---
    base_url = config['DEFAULT']['base_url']

    # Create the WebDriver instance
    driver = BrowserFactory.get_driver(browser, headless=headless)
    
    # --- Step 4: Navigate to the base_url ---
    driver.get(base_url)
    driver.maximize_window()

    # Pass the driver to the test class
    request.cls.driver = driver
    yield
    
    # Teardown: runs after all tests in the class are finished
    driver.quit()
