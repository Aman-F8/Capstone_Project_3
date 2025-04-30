import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Configuration.confest import driver
from Test_Data.data import Data
from selenium.common.exceptions import TimeoutException


'''
Test-case-6:    1) There are six product mentioned in the inventory. Choose any four products out of the six randomly using python. 
	            2) Add four product into the cart.
	            3) Verify the cart button has the four products.
'''

def test_add_random_products_to_cart(driver):

    driver.get(Data.URL)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'user-name'))).send_keys('standard_user')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    # Wait for the products to load
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'inventory_item')))
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')

    # Select 4 random products
    selected_products = random.sample(products, 4)

    # Add selected products to the cart
    print("Adding 4 random products to cart:")
    for product in selected_products:
        product_name = product.find_element(By.CLASS_NAME, 'inventory_item_name').text
        product_price = product.find_element(By.CLASS_NAME, 'inventory_item_price').text
        print(f"Added: {product_name} | {product_price}")
        product.find_element(By.CLASS_NAME, 'btn_inventory').click()

    # Wait for the cart page to load (use WebDriverWait for cart items to be visible)
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    try:
        # Wait for the cart items to be visible (instead of just presence)
        WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'cart_item')))
        cart_items = driver.find_elements(By.CLASS_NAME, 'cart_item')

        # Verify the number of items in the cart
        assert len(cart_items) == 4, f"Cart verification failed: Expected 4 items, but found {len(cart_items)}"
        print("Test passed: 4 items successfully added to the cart!")

    except TimeoutException:
        print("TimeoutException: Could not find cart items within the wait time.")
    finally:
        driver.quit()

