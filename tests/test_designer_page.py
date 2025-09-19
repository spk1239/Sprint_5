from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from locators import Locators
import pytest


class TestDesigner:

    @pytest.mark.parametrize("locator", [Locators.SAUCES_PAGE, Locators.ROLLS_PAGE, Locators.TOPPINGS_PAGE])
    def test_designer_page_aria_selected(self, driver,locator):

        driver.get(Data.STELLAR_BURGER_URL)

        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))

        driver.execute_script("arguments[0].click();", element)

        assert "tab_tab_type_current__2BEPc" in element.get_attribute("class") 



   
    