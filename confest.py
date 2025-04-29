"""
Use conftest.py to manage the webdriver setup and teardown
"""

import pytest                   # Importing pytest for testing and fixture support
from selenium import webdriver  # Importing Selenium WebDriver to control the browser
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    '''If i try this line, i'm facing error like driver not found'''
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    chrome_options = Options()

    # Disable "Show Notifications" popup
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=chrome_options)     # Launch a new Chrome browser instance
    driver.maximize_window()        # Maximize the browser window for better visibility

    yield driver                    # Yield the WebDriver instance to the test(s)

    driver.quit()                   # Quit the browser after all tests using this fixture are done