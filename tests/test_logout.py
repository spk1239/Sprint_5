from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from locators import Locators

class TestLogout:
    def test_logout_account(self, driver):

        driver.get(Data.STELLAR_BURGER_LOGIN_URL)
        
        driver.find_element(*Locators.EMAIL_INPUT).send_keys('test_email_adress@yandex.ru')

        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('qwerty123')

        driver.find_element(*Locators.BUTTON_LOGIN).click()
        
        driver.find_element(*Locators.LOGIN_ACCONT).click()

        logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.BUTTON_LOGOUT))
        logout_button.click()

        WebDriverWait(driver, 10).until(EC.url_contains("login"))
        current_url = driver.current_url
        
        assert "login" in current_url