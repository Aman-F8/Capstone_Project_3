import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Data.excel_data import ExcelReader
from Test_Locators.locators import WebLocators
from Test_Data.data import Data


# Test-case-01	1) Test whether you can able to login using username
#                  (standard_user, problem_user, performance_glitch_user, locked_out_user) and password (secret_sauce)
#               2) Check the login using cookies only. Do not use URL or page title.

# Read data from Excel
def get_test_data():
    excel_reader = ExcelReader(Data.EXCEL_FILE, Data.SHEET_NUMBER)
    rows = excel_reader.row_count()
    data = []
    for row in range(2, rows + 1):
        username = excel_reader.read_data(row, 6)
        password = excel_reader.read_data(row, 7)
        data.append((row, username, password))
    return data


@pytest.mark.parametrize("row,username,password", get_test_data())
def test_login_and_cookie_login(row, username, password):
    excel_reader = ExcelReader(Data().EXCEL_FILE, Data().SHEET_NUMBER)

    # Phase 1: Standard login
    driver = webdriver.Chrome()
    driver.get(Data().URL)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, WebLocators.Username)))
    driver.find_element(By.ID, WebLocators.Username).clear()
    driver.find_element(By.ID, WebLocators.Username).send_keys(username)
    driver.find_element(By.ID, WebLocators.Password).clear()
    driver.find_element(By.ID, WebLocators.Password).send_keys(password)
    driver.find_element(By.ID, WebLocators.Login_button).click()

    try:
        # Wait for inventory page
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
        print(f"SUCCESS: Login passed with USERNAME={username}")
        excel_reader.write_data(row, 8, "TEST PASSED")

        # Phase 2: Get cookies and login using cookies
        cookies = driver.get_cookies()
        driver.quit()

        driver = webdriver.Chrome()
        driver.get(Data().URL)
        driver.delete_all_cookies()

        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("https://www.saucedemo.com/inventory.html")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
        print("SUCCESS: Cookie-based login successful.")
        excel_reader.write_data(row, 9, "COOKIE LOGIN PASSED")

    except Exception as e:
        print(f"ERROR: Login or cookie-based login failed for USERNAME={username}")
        excel_reader.write_data(row, 8, "TEST FAILED")
        excel_reader.write_data(row, 9, "COOKIE LOGIN FAILED")
        assert False, str(e)

    finally:
        driver.quit()
