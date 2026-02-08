from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class FromToPageUrbanRoutes:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    def __init__(self, driver):
        self.driver = driver

    def __set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def __set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def wait_for_load_address_field(self):
        (WebDriverWait(self.driver, 5)
         .until(expected_conditions.visibility_of_element_located(self.from_field)))

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.__set_from(address_from)
        self.__set_to(address_to)