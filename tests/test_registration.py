from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from locators import Locators
from email_generator import email_generator

class TestRegistration:
    def test_registration_successful_registration(self, driver):

        driver.get(Data.STELLAR_BURGER_REGISTRATION_URL)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.NAME_REGISTRATION))

        driver.find_element(*Locators.NAME_REGISTRATION).send_keys('Никита')

        driver.find_element(*Locators.EMAIL_REGISTRATION).send_keys(email_generator())

        driver.find_element(*Locators.PASSWORD_REGISTRATION).send_keys('Nikita1997')

        driver.find_element(*Locators.BUTTON_REGISTRATION).click()

        current_url = driver.current_url

        assert "stellarburgers.nomoreparties.site/register" in current_url
        
        driver.quit()

    
    def test_registration_error_password_5_simbols(self,driver):

        driver.get(Data.STELLAR_BURGER_REGISTRATION_URL)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.NAME_REGISTRATION))

        driver.find_element(*Locators.NAME_REGISTRATION).send_keys('Никита')

        driver.find_element(*Locators.EMAIL_REGISTRATION).send_keys(email_generator())

        driver.find_element(*Locators.PASSWORD_REGISTRATION).send_keys('12345')

        driver.find_element(*Locators.BUTTON_REGISTRATION).click()

        error_text = driver.find_element(*Locators.ERROR_PASSWORD)

        assert error_text.is_displayed()
        
        driver.quit()