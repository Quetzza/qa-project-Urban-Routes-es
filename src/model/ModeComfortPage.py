from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import  time

class ModeComfortPage:

    service_comfort = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')

    def __init__(self, driver):
        self.driver = driver

    def set_mode_comfort(self):
        (WebDriverWait(self.driver,5)
         .until(expected_conditions.visibility_of_element_located(self.service_comfort))).click()
