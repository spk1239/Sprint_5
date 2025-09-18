from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from locators import Locators


class TestDesigner:
    
    def test_sauces_section_aria_selected(self, driver):

        driver.get(Data.STELLAR_BURGER_URL)

        driver.find_element(*Locators.SAUCES_PAGE).click()
        
        sauces_class = driver.find_element(*Locators.SAUCES_PAGE).get_attribute('class')

        assert "tab_tab__1SPyG tab_tab_type_current__2BEPc" in sauces_class

        driver.quit()


    def test_rolls_section_aria_selected(self, driver):

        driver.get(Data.STELLAR_BURGER_URL)

        driver.find_element(*Locators.SAUCES_PAGE).click()

        driver.find_element(*Locators.ROLLS_PAGE).click()
        
        rolls_class = driver.find_element(*Locators.ROLLS_PAGE).get_attribute('class')

        assert "tab_tab__1SPyG tab_tab_type_current__2BEPc" in rolls_class

        driver.quit()
    

    def test_toppings_section_aria_selected(self, driver):

        driver.get(Data.STELLAR_BURGER_URL)

        driver.find_element(*Locators.TOPPINGS_PAGE).click()
        
        toppings_class = driver.find_element(*Locators.TOPPINGS_PAGE).get_attribute('class')

        assert "tab_tab__1SPyG tab_tab_type_current__2BEPc" in toppings_class

        driver.quit()

    