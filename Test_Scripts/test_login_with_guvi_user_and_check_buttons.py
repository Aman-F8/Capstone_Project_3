import pytest

from Page_Objects.login_page import LoginPage
from Test_Data.data import Data
from Configuration.confest import driver


# Test-case-2	1) Test whether you can able to login using username (guvi_user)
#                  and password (secret@123)

def test_with_guvi_user(driver):

        # Open the GUVI homepage
        driver.get(Data.URL)
        # Create an instance of the LoginPage class
        login_page = LoginPage(driver)

        try:
            login_page.enter_username_password(Data.username, Data.password)

            if login_page.click_login():
                print(" SUCCESS: Login passed for GUVI user.")
            else:
                print(" FAILURE: Login failed for GUVI user.")

        except Exception as e:
            print(f" ERROR: Exception during login - {str(e)}")

        finally:
            driver.quit()


#Test-case-3	1) Test whether the logout button is functioning or not.

def test_logout_func(driver):
    driver.get(Data.URL)
    login_page = LoginPage(driver)

    try:
        login_page.enter_username_password("standard_user", "secret_sauce")

        if login_page.click_login():
            print(" Login successfully.")
            if login_page.click_logout():
                if login_page.is_logged_out():
                    print(" Logout successful.")
                else:
                    print(" Logout button clicked, but still logged in.")
    except Exception as e:
        print(f" ERROR during logout test: {str(e)}")

    finally:
        driver.quit()


#Test-case-3:    2) Test whether visibility of the login button.

def test_login_button(driver):

    try:
        # Open the target URL in the browser
        driver.get(Data.URL)
        login_page = LoginPage(driver)
        login_btn_link = login_page.check_login()
        assert login_btn_link, "[FAIL] Login button not visible"
    except Exception as e:
        print(f"[ERROR] Login button check failed: {e}")
        pytest.fail("Could not verify login button")


#Test-case-4:	1) Test whether the cart button is visible or not.

def test_cart_button(driver):

    try:
        # Open the target URL in the browser
        driver.get(Data.URL)
        login_page = LoginPage(driver)
        login_page.enter_username_password("standard_user", "secret_sauce")
        login_page.click_login()
        cart_btn_link = login_page.check_cart()
        assert cart_btn_link, "[FAIL] Cart button not visible"
    except Exception as e:
        print(f"[ERROR] Cart button check failed: {e}")
        pytest.fail("Could not verify Cart button")

