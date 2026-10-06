from selenium.webdriver.common.by import By #localiza cualquier selector mediante

URL_LOGIN = 'https://www.saucedemo.com/' 


def login_helper(driver):
    driver.get(URL_LOGIN)
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    