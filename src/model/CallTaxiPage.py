import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class CallTaxiPage:

    route_mode = (By.XPATH, '//div[@class="mode active" and text()="Flash"]')
    transport = (By.XPATH, '//div[@class="type active disabled"]/img[@class="type-icon"]')
    call_taxi_button = (By.XPATH, '//button[@class="button round"]')

    def __init__(self, drive):
        self.driver = drive

    #Optimo - Flash - Personal
    def __get_default_mode_route(self):
        return self.driver.find_element(*self.route_mode).text

    # car - walk - taxi - bike - scooter - drive
    def __get_default_mode_of_transport(self):
        return self.driver.find_element(*self.transport).get_attribute('src')

    def call_taxi(self):
        assert self.__get_default_mode_route() == 'Flash'# check the default selected mode route 'Flash'
        assert 'car' in self.__get_default_mode_of_transport()# check the default selected service fee 'taxi'
        (WebDriverWait(self.driver,5)
         .until(expected_conditions
                .visibility_of_element_located(self.call_taxi_button))).click()


