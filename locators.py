from selenium.webdriver.common.by import By

locators = {
    "Button_Personal_account": (By.XPATH,"//*[text()='Личный Кабинет']"),  #кнопка Личный кабинет
    "Button_Login_to_account": (By.XPATH, "//button[text()='Войти в аккаунт']"),  #кнопка Войти в аккаунт
    "Button_Register": (By.XPATH, "//a[text()='Зарегистрироваться']"),  #кнопка Зарегистироваться
    "Button_Reset_Password": (By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/forgot-password']"), #кнопка Восстановить пароль
    "Field_Name": (By.XPATH, "//fieldset[1]//input[@name='name']"),  #поле с именем
    "Field_Email": (By.XPATH, "//fieldset[2]//input[@name='name']"),  #поле с email
    "Field_Password": (By.XPATH, "//input[@name='Пароль']"),  #поле с паролем
    "Register_button_2": (By.XPATH, '//button[text()="Зарегистрироваться"]'),
    "Button_Login": (By.XPATH, "//button[text()='Войти']"),  #кнопка Войти
    "Button_Login_in_registration": (By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login']"),  #кнопка Войти на странице регистрации/восстановления пароля
    "Button_Logout": (By.XPATH, "//button[text()='Выход']"),  #кнопка Выход
    "Button_Constructor": (By.XPATH, "//header//li[1]/a"),  #кнопка Конструктор (а)
    "Button_Logotype_Stellar_Burgers": (By.XPATH, "//div[contains( @class, 'AppHeader_header')]"),  #кнопка логотипа на хэдере
    "Button_Buns": (By.XPATH, "//span[text()='Булки']"),  #кнопка Булки на панеле
    "Button_Sauces": (By.XPATH, "//span[text()='Соусы']"),  #кнопка Соусы на панеле
    "Button_Stuffings": (By.XPATH, "//span[text()='Начинки']"),  #кнопка Начинки на панеле
    "Title_Buns": (By.XPATH, "//h2[text()='Булки']"),  # заголовок Булки в блоке
    "Title_Sauces": (By.XPATH, "//h2[text()='Соусы']"),  # заголовок Соусы в блоке
    "Title_Stuffings": (By.XPATH, "//h2[text()='Начинки']"),  # заголовок Начинки в блоке
}
