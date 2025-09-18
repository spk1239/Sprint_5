from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from locators import Locators


class TestLoginToAccount:
    def test_login_in_personal_account(self, driver):

        driver.get(Data.STELLAR_BURGER_URL)

        driver.find_element(*Locators.LOGIN_ACCONT).click()

        driver.find_element(*Locators.EMAIL_INPUT).send_keys('test_email_adress@yandex.ru')

        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('qwerty123')

        driver.find_element(*Locators.BUTTON_LOGIN).click()

        driver.find_element(*Locators.LOGIN_ACCONT).click()

        current_url = driver.current_url

        assert "site/account" in current_url

        driver.quit()

    
    def test_login_in_main_page(self, driver):

        driver.get(Data.STELLAR_BURGER_URL)

        driver.find_element(*Locators.BUTTON_LOG_IN_ACCOUNT).click()

        driver.find_element(*Locators.EMAIL_INPUT).send_keys('test_email_adress@yandex.ru')

        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('qwerty123')

        driver.find_element(*Locators.BUTTON_LOGIN).click()

        driver.find_element(*Locators.LOGIN_ACCONT).click()

        current_url = driver.current_url

        assert "site/account" in current_url

        driver.quit()

    
    def test_login_in_registration_page(self, driver):

        driver.get(Data.STELLAR_BURGER_REGISTRATION_URL)

        driver.find_element(*Locators.BUTTON_LOG_IN_REGISTRATION).click()

        driver.find_element(*Locators.EMAIL_INPUT).send_keys('test_email_adress@yandex.ru')

        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('qwerty123')

        driver.find_element(*Locators.BUTTON_LOGIN).click()

        driver.find_element(*Locators.LOGIN_ACCONT).click()

        current_url = driver.current_url

        assert "site/account" in current_url

        driver.quit()

    
    def test_login_in_password_recovery_page(self, driver):

        driver.get(Data.STELLAR_BURGER_URL)

        driver.find_element(*Locators.BUTTON_LOG_IN_ACCOUNT).click()
        
        driver.find_element(*Locators.BUTTON_PASSWORD_RECOVERY ).click()

        driver.find_element(*Locators.BUTTON_LOG_IN_PASSWORD_RECOVERY).click()

        driver.find_element(*Locators.EMAIL_INPUT).send_keys('test_email_adress@yandex.ru')

        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('qwerty123')

        driver.find_element(*Locators.BUTTON_LOGIN).click()

        driver.find_element(*Locators.LOGIN_ACCONT).click()

        current_url = driver.current_url

        assert "site/account" in current_url

        driver.quit()