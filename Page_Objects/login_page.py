from selenium.webdriver.common.by import By
from Page_Objects.base_page import BasePage
from Test_Locators.locators import WebLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    # Define locators for different elements on the page

    USERNAME = (By.NAME, WebLocators.Username)
    PASSWORD = (By.NAME, WebLocators.Password)
    LOGIN_BUTTON = (By.ID, WebLocators.Login_button)
    MENU_BUTTON = (By.ID, WebLocators.Menu_Button)
    LOGOUT_BUTTON = (By.ID, WebLocators.Logout)
    CART = (By.CLASS_NAME, WebLocators.Cart)

    # Enters the given email into the email input field
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = None

    def enter_username_password(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def click_logout(self):
        try:
            burger_button = self.wait.until(EC.presence_of_element_located((By.XPATH, WebLocators.Menu_Button)))
            burger_button.click()
            logout_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, WebLocators.Logout))
            )
            logout_btn.click()
            return True
        except:
            return False

    def is_logged_out(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, WebLocators.Username)))
            return True
        except:
            return False

    def check_login(self):
        return self.is_visible(self.LOGIN_BUTTON)

    def check_cart(self):
        return self.is_visible(self.CART)






