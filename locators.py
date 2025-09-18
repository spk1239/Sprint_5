from selenium.webdriver.common.by import By

class Locators:

    BUTTON_IN_ACCOUNT = (By.XPATH, ".//div/button[1]") #Кнопка перехода "Войти в аккаунт"

    BUTTON_IN_REGISTRATION = (By.XPATH, ".//div/p[1]/a") #Кнопка перехода "Зарегистрироваться"

    NAME_REGISTRATION = (By.XPATH, ".//form/fieldset[1]/div/div/input") #Поле в регистрации "Имя"

    EMAIL_REGISTRATION = (By.XPATH, ".//form/fieldset[2]/div/div/input") #Поле в регистрации "Email"

    PASSWORD_REGISTRATION = (By.XPATH, ".//form/fieldset[3]/div/div/input") #Поле в регистрации "Пароль"

    BUTTON_REGISTRATION = (By.XPATH, ".//form/button") #Кнопка "Зарегистрироваться"

    ERROR_PASSWORD = (By.CLASS_NAME, "input__error") #Ошибка "Некорректный пароль"

    LOGIN_ACCONT = (By.XPATH, ".//div/header/nav/a/p") #Кнопка перехода "Личный кабинет"

    EMAIL_INPUT = (By.XPATH, ".//form/fieldset[1]/div/div/input") # Поле входа "Email"

    PASSWORD_INPUT = (By.XPATH, ".//form/fieldset[2]/div/div/input") # Поле входа "Пароль"

    BUTTON_LOGIN = (By.XPATH, ".//main/div/form/button") #Кнопка входа, в Личном кабинете

    BUTTON_LOG_IN_ACCOUNT = (By.XPATH, ".//main/section[2]/div/button") #Кнопка входа, на Главной страницы

    BUTTON_LOG_IN_REGISTRATION = (By.CLASS_NAME, "Auth_link__1fOlj") #Кнопка входа, на странице регистрации

    BUTTON_LOG_IN_PASSWORD_RECOVERY = (By.XPATH, ".//main/div/div/p/a") #Кнопка входа, на странице восстановления пароля

    BUTTON_PASSWORD_RECOVERY = (By.XPATH, ".//div/main/div/div/p[2]/a") #Кнопка перехода на страницу восстановления пароля

    BUTTON_DESIGNER = (By.XPATH, ".//header/nav/ul/li[1]/a/p") #Кнопка перехода в Конструктор

    LOGO_BURGERS = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # Логотип "StarBurgers"

    BUTTON_LOGOUT = (By.CLASS_NAME, "Account_button__14Yp3") #Кнопка выхода из аккаунта

    SAUCES_PAGE = (By.XPATH, ".//main/section[1]/div[1]/div[2]") #Раздел Соусов

    ROLLS_PAGE = (By.XPATH, ".//main/section[1]/div[1]/div[1]") #Раздел Булки

    TOPPINGS_PAGE = (By.XPATH, ".//main/section[1]/div[1]/div[3]") #Начинки
