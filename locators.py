from selenium.webdriver.common.by import By

class Locators:

    BUTTON_IN_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']") #Кнопка перехода "Войти в аккаунт"

    BUTTON_IN_REGISTRATION = (By.XPATH, "//a[text()='Зарегистрироваться']") #Кнопка перехода "Зарегистрироваться"

    NAME_REGISTRATION = (By.XPATH, "//label[text()='Имя']/following::input") #Поле в регистрации "Имя"

    EMAIL_REGISTRATION = (By.XPATH, "//label[text()='Email']/following::input") #Поле в регистрации "Email"

    PASSWORD_REGISTRATION = (By.XPATH, "//input[@type='password']") #Поле в регистрации "Пароль"

    BUTTON_REGISTRATION = (By.XPATH, "//button[text()='Зарегистрироваться']") #Кнопка "Зарегистрироваться"

    ERROR_PASSWORD = (By.CLASS_NAME, "input__error") #Ошибка "Некорректный пароль"

    LOGIN_ACCONT = (By.XPATH, ".//p[text()='Личный Кабинет']") #Кнопка перехода "Личный кабинет"

    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following::input") # Поле входа "Email"

    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following::input") # Поле входа "Пароль"

    BUTTON_LOGIN = (By.XPATH, ".//button[text()='Войти']") #Кнопка входа, в Личном кабинете

    BUTTON_LOG_IN_REGISTRATION = (By.CLASS_NAME, "Auth_link__1fOlj") #Кнопка входа, на странице регистрации

    BUTTON_LOG_IN_PASSWORD_RECOVERY = (By.XPATH, ".//a[text()='Войти']") #Кнопка входа, на странице восстановления пароля

    BUTTON_PASSWORD_RECOVERY = (By.XPATH, ".//a[text()='Восстановить пароль']") #Кнопка перехода на страницу восстановления пароля

    BUTTON_DESIGNER = (By.XPATH, ".//p[text()='Конструктор']") #Кнопка перехода в Конструктор

    LOGO_BURGERS = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # Логотип "StarBurgers"

    BUTTON_LOGOUT = (By.CLASS_NAME, "Account_button__14Yp3") #Кнопка выхода из аккаунта

    SAUCES_PAGE = (By.XPATH, ".//span[text()='Соусы']/parent::div") #Раздел Соусов

    ROLLS_PAGE = (By.XPATH, ".//span[text()='Булки']/parent::div") #Раздел Булки

    TOPPINGS_PAGE = (By.XPATH, ".//span[text()='Начинки']/parent::div") #Начинки
