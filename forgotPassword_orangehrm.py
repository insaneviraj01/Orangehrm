from selenium import webdriver
from selenium.webdriver.common.by import By



def forgot_password_orangehrm():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print(f"Web title:{driver.title}")
    print(driver.current_url)
    driver.find_element(By.CSS_SELECTOR,".orangehrm-login-forgot-header").click()
    driver.find_element(By.CSS_SELECTOR,".oxd-input--active").send_keys("Admin")
    driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    msg  = driver.find_element(By.CSS_SELECTOR,"div[class='orangehrm-card-container'] h6").text
    expected_msg = "Reset Password link sent successfully"
    actual_msg = msg
    assert expected_msg ==actual_msg
    print(f"assertion is pass:{"Expected msg is",expected_msg}:{"Actual msg is",actual_msg}")
forgot_password_orangehrm()



