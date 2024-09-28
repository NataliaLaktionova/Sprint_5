from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import locators
from conftest import driver
from personal_data import Personal_data

def test_successful_registration(driver):
    wait = WebDriverWait(driver, 20)
    wait.until(EC.element_to_be_clickable(locators["Button_Login_to_account"])).click()
    wait.until(EC.element_to_be_clickable(locators["Button_Register"])).click()

    name_field = wait.until(EC.presence_of_element_located(locators["Field_Name"]))
    name_field.send_keys(Personal_data.name)

    email_field = wait.until(EC.presence_of_element_located(locators["Field_Email"]))
    email_field.send_keys(Personal_data.email)

    password_field = wait.until(EC.presence_of_element_located(locators["Field_Password"]))
    password_field.send_keys(Personal_data.password)

    register_button = wait.until(EC.element_to_be_clickable(locators["Register_button_2"]))
    register_button.click()
    assert 'https://stellarburgers.nomoreparties.site/' in driver.current_url


def test_with_incorrect_password(driver):
    wait = WebDriverWait(driver, 20)
    wait.until(EC.element_to_be_clickable(locators["Button_Login_to_account"])).click()
    wait.until(EC.element_to_be_clickable(locators["Button_Register"])).click()

    name_field = wait.until(EC.presence_of_element_located(locators["Field_Name"]))
    name_field.send_keys(Personal_data.name)

    email_field = wait.until(EC.presence_of_element_located(locators["Field_Email"]))
    email_field.send_keys(Personal_data.email)

    password_field = wait.until(EC.presence_of_element_located(locators["Field_Password"]))
    password_field.send_keys(Personal_data.incorrect_password)

    register_button = wait.until(EC.element_to_be_clickable(locators["Register_button_2"]))
    register_button.click()

    error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")))
    assert error_message.is_displayed(), "Сообщение об ошибке не отображается при невалидном пароле!"


