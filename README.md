Project Title:
Automating the Web Application https://www.saucedemo.com using Python Selenium & Pytest Framework

Objective:
To build a hybrid test automation framework using Python, Selenium, Pytest, Page Object Model (POM), Data-Driven Testing (DDT), and Keyword-Driven Testing (KDT) to validate functionality of the e-commerce platform https://www.saucedemo.com including login, logout, product selection, cart management, and checkout flow.

Tools & Technologies Used:
Language: Python 3.x (OOP-based structure)

Browser Automation: Selenium WebDriver

Test Runner: Pytest

Framework Structure: Hybrid (POM + DDT with Excel/CSV + KDT with YAML)

Wait Strategy: Explicit Wait (WebDriverWait)

Reporting: HTML report using pytest-html

Testing Browsers: Chrome, Firefox, Edge

Exception Handling: Python Try-Except blocks

Code Quality: Pylint conventions followed

Version Control: GitHub

Documentation: README.md with full project structure explanation

Recording Tool: OBS Studio or Snipping Tool for demonstration video

🧪 Test Suite Overview:

Test Case ID	Test Description	Status
TC-01	Login with multiple valid/invalid users using DDT & verify via cookies	✅
TC-02	Login with non-existing user (guvi_user) and validate	✅
TC-03	Validate Logout button functionality and Login button visibility	✅
TC-04	Check visibility of the cart button	✅
TC-05	Randomly select 4 products and fetch their name & price	✅
TC-06	Add 4 random products to cart and validate item count	✅
TC-07	Validate product details in cart	✅
TC-08	Fill checkout form, take screenshot, complete order, and validate confirmation	✅
Framework Structure (Example):

saucedemo_automation/
│
├── config/
│   └── confest.py
│
├── page_object
│   ├── base_page.py
│   └── login_page.py
|
├── Reports
│   └── reports.html
|
├── Test_data
│   ├── data.py
│   └── excel_data.py
|
|── Test_Locators
│   └── locators.py
|
├── Test_Scripts
│   ├── test_add_random_products.py
│   ├── test_add_to_cart.py
│   ├── test_complete_order.py
|   ├── test_login_with_cookie.py
|   ├──test_login_with_guvi_user_and_check_buttons.py
│   └── test_product_in_cart.py
│
├── screenshots/
│   └── checkout_overview.png
│
├──Prject_report_3.xlsx

📷 Deliverables:
Complete Hybrid Framework with Python OOP, POM, DDT, KDT

HTML Pytest Report for each test case

Screenshot captured for checkout overview

Uploaded project with proper structure on GitHub

README.md describing project structure, setup, and usage

Would you like a template to start coding this framework, including folder structure, sample test, and YAML/DDT example?
