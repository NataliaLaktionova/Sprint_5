from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import locators
from conftest import driver

def test_redirect_to_sauces(driver):
    wait = WebDriverWait(driver, 15)
    wait.until(EC.element_to_be_clickable(locators["Button_Sauces"])).click()
    assert wait.until(EC.visibility_of_element_located(locators["Title_Sauces"])), "Title 'Соусы' is not visible."

def test_redirect_to_stuffings(driver):
    wait = WebDriverWait(driver, 15)
    wait.until(EC.element_to_be_clickable(locators["Button_Stuffings"])).click()
    assert wait.until(EC.visibility_of_element_located(locators["Title_Stuffings"])), "Title 'Начинки' is not visible."

def test_redirect_from_stuffings_to_bun(driver):
    wait = WebDriverWait(driver, 15)
    wait.until(EC.element_to_be_clickable(locators["Button_Stuffings"])).click()
    wait.until(EC.element_to_be_clickable(locators["Button_Buns"])).click()
    assert wait.until(EC.visibility_of_element_located(locators["Title_Buns"])), "Title 'Булки' is not visible."