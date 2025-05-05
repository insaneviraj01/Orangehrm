import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def login_orangehrm():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print(f"Web URL:{driver.current_url}")
    actual_web_title = driver.title
    expected_web_title = "OrangeHRM"
    assert actual_web_title == expected_web_title
    print(f"Web Title:{driver.title}")
    driver.maximize_window()
    driver.implicitly_wait(5)
    userName = driver.find_element(By.CSS_SELECTOR,"div [class='orangehrm-login-error'] p:nth-child(1)")
    userName = userName.text
    print(f"Username text is:{userName}")
    user = userName.split(":")[1].strip()
    print(f"Username name is:{userName[11::]}")
    driver.find_element(By.XPATH,"//input[@name='username']").send_keys(user)
    password = driver.find_element(By.CSS_SELECTOR,"div [class='orangehrm-login-error'] p:nth-child(2)")
    password = password.text
    print(f"password text is:{password}")
    key = password.split(":")[1].strip()
    print(f"Username name is:{password[11::]}")
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys(key)
    driver.find_element(By.CLASS_NAME,"oxd-button").click()
    user_Profile_Name  = driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name").text
    print(f"User name is:{user_Profile_Name}")

    if user_Profile_Name == user_Profile_Name:
        assert user_Profile_Name == user_Profile_Name
        print(f"Assertion pass user name is:{user_Profile_Name}")
    else:
        print("Assertion fail")

    print(f"After login url:{driver.current_url}")
    print(f"After login page title:{driver.title}")
    driver.quit()
login_orangehrm()


