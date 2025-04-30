# PAT Capstone Project: Automating SauceDemo with Python Selenium & Pytest

**Title:**  
Automating the [SauceDemo](https://www.saucedemo.com/) web application using a hybrid testing framework built on **Python Selenium**, **Pytest**, **POM**, **DDT**, and **Keyword-Driven Testing**.

---

## Project Summary

This capstone project aims to automate functional test cases for [SauceDemo](https://www.saucedemo.com/) 
using a structured and scalable automation framework. The project leverages **Page Object Model (POM)**, **Object-Oriented Programming**, and **Data-Driven Testing** with Excel inputs. 
Explicit waits ensure stable interaction with dynamic content, while **Pytest-based HTML reports** offer detailed insights into test execution. 
Scenarios include login tests, cart validation, product verification, and order confirmation with screenshot capture.

---

## Test Objective

Build a robust automation framework to:
- Verify login functionality with various user roles.
- Interact with shopping cart and product inventory.
- Validate checkout and order flow.
- Capture screenshots and generate reports for all test cases.
- Implement **cookies-based login validation**.
- Use **random selection logic** for product testing.

---

## Tools & Technologies

- **Python 3**
- **Selenium WebDriver**
- **Pytest**
- **Page Object Model (POM)**
- **Data-Driven Testing (DDT)**
- **Keyword-Driven Hybrid Framework**
- **Explicit Waits**
- **HTML Reporting (pytest-html)**
- **Pylint** (for naming conventions and code style)

---

## Target URL

> [https://www.saucedemo.com/](https://www.saucedemo.com/)

---

## Precondition

All test cases are written to cover **positive and negative scenarios** and adhere to **OOP**, **POM**, **DDT**, and **pylint-compliant** naming conventions.

---

## Test Suite

### **Test Case 01: Login with Different Users + Cookie Validation**
1. Login using the following users and password `secret_sauce`:
   - `standard_user`
   - `problem_user`
   - `performance_glitch_user`
   - `locked_out_user`
2. Verify login using **cookies only**, not URL or title.
3. Generate **pytest-based HTML report**.

---

### **Test Case 02: Invalid User Login**
1. Attempt login with `guvi_user` and password `secret@123`.
2. Generate **pytest-based HTML report**.

---

### **Test Case 03: Logout Functionality**
1. Verify if the **logout button** works.
2. Check if the **login button** becomes visible again.
3. Generate **pytest-based HTML report**.

---

### **Test Case 04: Cart Button Visibility**
1. Check whether the **cart button** is visible.
2. Generate **pytest-based HTML report**.

---

### **Test Case 05: Random Product Selection & Price Fetch**
1. There are 6 products in inventory — choose any 4 **randomly using Python logic** (not manual).
2. Fetch and print **product names** and **prices**.
3. Generate **pytest-based HTML report**.

---

### **Test Case 06: Add Random Products to Cart**
1. Select 4 random products from the inventory.
2. Add those products to the cart.
3. Verify the **cart icon shows count = 4**.
4. Generate **pytest-based HTML report**.

---

### **Test Case 07: Cart Content Verification**
1. Click the **cart button**.
2. Fetch product details added to the cart.
3. Generate **pytest-based HTML report**.

---

### **Test Case 08: Checkout Process & Screenshot**
1. Click the **checkout** button.
2. Fill in:
   - First name
   - Last name
   - Zip code
3. Click **continue** and take a **screenshot** of the checkout overview (PNG/JPG).
4. Press the **finish** button and confirm completion.
5. Generate **pytest-based HTML report**.

---
