from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Configuration.confest import driver
from Test_Data.data import Data


'''
Test-case-8:
    1) Click the check button, add you details like first name, last name and pin code/zipcode into given input boxes and click the continue button.
	2) download the screenshot of the checkout overview in the form of PNG/JPEG/JPG format.
	3) Press the finish button, and get the confirmation for your action.
'''

def test_checkout_and_screenshot(driver):
    driver.get(Data.URL)

    # Step 1: Login
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, 'user-name'))).send_keys('standard_user')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, 'password'))).send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    # Step 2: Add a product
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'inventory_item')))
    driver.find_element(By.CLASS_NAME, 'btn_inventory').click()

    # Step 3: Go to cart
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    # Step 4: Click Checkout
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'checkout'))).click()

    # Step 5: Fill user info
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'first-name'))).send_keys('John')
    driver.find_element(By.ID, 'last-name').send_keys('Doe')
    driver.find_element(By.ID, 'postal-code').send_keys('12345')
    driver.find_element(By.ID, 'continue').click()

    # Step 6: Screenshot of Checkout Overview
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'summary_info')))
        screenshot_path = "./checkout_overview.png"
        driver.save_screenshot(screenshot_path)
        print(f" Screenshot saved: {screenshot_path}")
    except TimeoutException:
        print(" Timeout: Could not load checkout overview page.")

    # Step 7: Finish Order
    driver.find_element(By.ID, 'finish').click()

    # Step 8: Confirm Order Completion
    try:
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'complete-header')))
        message = driver.find_element(By.CLASS_NAME, 'complete-header').text
        print(f"\n Order Complete! Message: {message}")
        assert "THANK YOU" in message.upper()
    except TimeoutException:
        print(" Timeout: Finish confirmation not found.")
    finally:
        driver.quit()
