from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import locators
from conftest import driver
from personal_data import Personal_data

# вход по кнопке «Войти в аккаунт» на главной
def test_successful_login_to_account(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(locators["Button_Login_to_account"])).click()

    email_field = wait.until(EC.presence_of_element_located(locators["Field_Name"]))
    email_field.send_keys(Personal_data.email)

    password_field = wait.until(EC.presence_of_element_located(locators["Field_Password"]))
    password_field.send_keys(Personal_data.password)

    login_button = wait.until(EC.element_to_be_clickable(locators["Button_Login"]))
    login_button.click()
    assert 'https://stellarburgers.nomoreparties.site/' in driver.current_url

# вход через кнопку «Личный кабинет»
def test_successful_login_from_personal_cabinet(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(locators["Button_Personal_account"])).click()

    email_field = wait.until(EC.presence_of_element_located(locators["Field_Name"]))
    email_field.send_keys(Personal_data.email)

    password_field = wait.until(EC.presence_of_element_located(locators["Field_Password"]))
    password_field.send_keys(Personal_data.password)

    login_button = wait.until(EC.element_to_be_clickable(locators["Button_Login"]))
    login_button.click()
    assert 'https://stellarburgers.nomoreparties.site/' in driver.current_url

# вход через кнопку в форме регистрации
def test_successful_login_registration_form(driver):
    wait = WebDriverWait(driver, 15)
    wait.until(EC.element_to_be_clickable(locators["Button_Login_to_account"])).click()
    wait.until(EC.element_to_be_clickable(locators["Button_Register"])).click()
    wait.until(EC.element_to_be_clickable(locators["Button_Login_in_registration"])).click()

    email_field = wait.until(EC.presence_of_element_located(locators["Field_Name"]))
    email_field.send_keys(Personal_data.email)

    password_field = wait.until(EC.presence_of_element_located(locators["Field_Password"]))
    password_field.send_keys(Personal_data.password)

    login_button = wait.until(EC.element_to_be_clickable(locators["Button_Login"]))
    login_button.click()
    assert 'https://stellarburgers.nomoreparties.site/' in driver.current_url

# вход через кнопку в форме восстановления пароля
def test_successful_login_password_reset_form(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(locators["Button_Login_to_account"])).click()
    wait.until(EC.element_to_be_clickable(locators["Button_Reset_Password"])).click()
    wait.until(EC.element_to_be_clickable(locators["Button_Login_in_registration"])).click()

    email_field = wait.until(EC.presence_of_element_located(locators["Field_Name"]))
    email_field.send_keys(Personal_data.email)

    password_field = wait.until(EC.presence_of_element_located(locators["Field_Password"]))
    password_field.send_keys(Personal_data.password)

    login_button = wait.until(EC.element_to_be_clickable(locators["Button_Login"]))
    login_button.click()
    assert 'https://stellarburgers.nomoreparties.site/' in driver.current_url