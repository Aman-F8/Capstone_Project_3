import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Locators.locators import WebLocators
from Test_Data.data import Data
from Configuration.confest import driver


#Test-case-5	1) There are six product mentioned in the inventory. Choose any four products out of the six randomly using python.
#               2) Fetch the product Name and price
def login_to_shopping_site(driver):
    driver.get(Data.URL)
    wait = WebDriverWait(driver, 10)

    #try:
        # Step 1: Open SauceDemo and login
        #driver.get("https://www.saucedemo.com/")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, WebLocators.Username))).send_keys("standard_user")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, WebLocators.Password))).send_keys("secret_sauce")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, WebLocators.Login_button))).click()

    # Step 2: Wait for inventory to load
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

def test_randomly_add_four_product(driver):
    login_to_shopping_site(driver)
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    print(f" Total products found: {len(products)}")

    # Step 4: Randomly select 4 products
    selected_products = random.sample(products, 4)

    print(" Selected 4 random products:")
    for product in selected_products:
        name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
        price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
        print(f" Product: {name}, Price: {price}")

    #except Exception as e:
        #print(f" ERROR: {str(e)}")

    # finally:
    #     driver.quit()
