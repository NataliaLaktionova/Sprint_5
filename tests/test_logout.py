from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import locators
from conftest import driver
from personal_data import Personal_data

def test_logout(driver):
    wait = WebDriverWait(driver, 15)
    wait.until(EC.element_to_be_clickable(locators["Button_Login_to_account"])).click()

    email_field = wait.until(EC.presence_of_element_located(locators["Field_Name"]))
    email_field.send_keys(Personal_data.email)

    password_field = wait.until(EC.presence_of_element_located(locators["Field_Password"]))
    password_field.send_keys(Personal_data.password)

    login_button = wait.until(EC.element_to_be_clickable(locators["Button_Login"]))
    login_button.click()
    wait.until(EC.element_to_be_clickable(locators["Button_Personal_account"])).click()
    wait.until(EC.element_to_be_clickable(locators["Button_Logout"])).click()

    wait.until(EC.element_to_be_clickable(locators["Button_Login"]))
    assert 'https://stellarburgers.nomoreparties.site/login' in driver.current_url