from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Configuration.confest import driver
from Test_Data.data import Data




# Test-case-7:	1) Click the cart button to verify the products that you have added into it.
# 	            2) Fetch the product details from the cart


def test_verify_cart_contents(driver):
    driver.get(Data.URL)

    # Login
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'user-name'))).send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    # Add two products to cart (for demo)
    products = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="inventory_list"]//button[contains(text(), "Add to cart")]')))

    for product in products[:4]:  # Adding only 4 products
        product.click()
        # product.find_element(By.CLASS_NAME, 'btn_inventory').click()

    # Click on Cart Button
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    # Fetch product details from Cart
    cart_items = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'cart_item')))
    # cart_items = driver.find_elements(By.CLASS_NAME, 'cart_item')

    print("\nProducts in Cart:")
    for item in cart_items:
        name = item.find_element(By.CLASS_NAME, 'inventory_item_name').text
        price = item.find_element(By.CLASS_NAME, 'inventory_item_price').text
        print(f"- {name}: {price}")

    assert len(cart_items) == 4, f"Expected 4 items in cart but found {len(cart_items)}"

    driver.quit()
