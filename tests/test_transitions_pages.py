from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from locators import Locators


class TestTransistionsPages:

    def test_transition_login_account(self, driver):

        driver.get(Data.STELLAR_BURGER_URL)
        
        driver.find_element(*Locators.LOGIN_ACCONT).click()

        current_url = driver.current_url

        assert ".site/login" in current_url

        driver.quit()
    
    
    def test_transition_designer(self, driver):
        
        driver.get(Data.STELLAR_BURGER_LOGIN_URL)

        driver.find_element(*Locators.BUTTON_DESIGNER).click()

        current_url = driver.current_url

        assert current_url == "https://stellarburgers.nomoreparties.site/"

        driver.quit()

    
    def test_transition_logo(self, driver):

        driver.get(Data.STELLAR_BURGER_LOGIN_URL)

        driver.find_element(*Locators.LOGO_BURGERS).click()
        
        current_url = driver.current_url

        assert current_url == "https://stellarburgers.nomoreparties.site/"

        driver.quit()

