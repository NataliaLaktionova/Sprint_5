Stellar Burgers - Автоматизированные Тесты
Stellar Burgers — это космический фастфуд, где пользователи могут собирать и заказывать бургеры из необычных ингредиентов. В этом проекте реализованы автоматизированные тесты для проверки функциональности сервиса.

Данный проект содержит набор тестов, написанных с использованием библиотеки Selenium и библиотеки pytest. Тесты предназначены для проверки основных функций веб-приложения Stellar Burgers, включая регистрацию, вход в аккаунт, навигацию и функциональность разделов.

Регистрация (test_registration)
-Проверка успешной регистрации с:
  -Непустым полем «Имя».
  - Корректным email в формате логин@домен (например, 123@ya.ru).
  - Минимальным паролем из шести символов.
- Проверка сообщения об ошибке для некорректного пароля.

Вход в аккаунт (test_login)
- Проверка входа по кнопке «Войти в аккаунт» на главной странице.
- Проверка входа через кнопку «Личный кабинет».
- Проверка входа через кнопку в форме регистрации.
- Проверка входа через кнопку в форме восстановления пароля.

Переход в личный кабинет (test_redirect_personal_account) 
- Проверка перехода по клику на «Личный кабинет».

Переход в конструктор бургеров (test_redirect_constructor_or_logotype)
- Проверка перехода по клику на «Конструктор».
- Проверка перехода по клику на логотип Stellar Burgers.

Выход из аккаунта (test_logout)
- Проверка выхода по кнопке «Выйти» в личном кабинете.

Раздел «Конструктор» (test_navigation_to_sections)
Проверка работоспособности переходов к разделам:
  - «Булки».
  - «Соусы».
  - «Начинки».