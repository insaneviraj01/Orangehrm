from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def login_orangehrm():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(5)

    # Enter demo credentials
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CLASS_NAME, "oxd-button").click()

    time.sleep(3)  # Replace with WebDriverWait in production

    # Click user dropdown
    driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()

    # Call logout
    logout_orangehrm()

def logout_orangehrm():
    driver.find_element(By.CSS_SELECTOR, "ul.oxd-dropdown-menu li:nth-child(4)").click()
    print("Logout successful")
    driver.quit()

# Run the login function
login_orangehrm()
