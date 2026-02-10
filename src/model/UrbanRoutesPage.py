from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions
class UrbanRoutesPage:

    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    route_mode = (By.XPATH, '//div[@class="mode active" and text()="Flash"]')
    transport = (By.XPATH, '//img[contains(@src, "taxi-active")]')
    call_taxi_button = (By.XPATH, '//button[@class="button round"]')

    service_active = (By.XPATH, '//div[@class="tcard active"]/div[@class="tcard-title"]')
    service_comfort = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')

    phone_field = (By.CLASS_NAME, "np-text")
    phone_input = (By.ID, 'phone')
    next_button = (By.XPATH, '//button[@class="button full" and text()="Next"]')
    code_input = (By.ID, 'code')
    confirm_button = (By.XPATH, '//button[@class="button full" and text()="Confirmar"]')

    def __init__(self, driver):
        self.driver = driver
    """
        Address section
    """
    def __set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def __set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def __wait_for_load_address_field(self):
        (WebDriverWait(self.driver, 5)
         .until(expected_conditions.visibility_of_element_located(self.from_field)))

    def get_from_value(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to_value(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.__wait_for_load_address_field()
        self.__set_from(from_address)
        self.__set_to(to_address)

    """
        Call taxi section
    """

    def get_default_mode_route(self):
        return (WebDriverWait(self.driver,5)
                .until(expected_conditions.visibility_of_element_located(self.route_mode))) # Flash

    def get_default_transport(self):
        return (WebDriverWait(self.driver,5)
                .until(expected_conditions.visibility_of_element_located(self.transport))).get_attribute('src')# taxi-active

    def __on_click_call_taxi(self):
        self.driver.find_element(*self.call_taxi_button).click()

    def call_taxi(self):
        self.__on_click_call_taxi()

    """
        Service fee section
    """

    def get_service_mode(self):
        return (WebDriverWait(self.driver,5)
                .until(expected_conditions.visibility_of_element_located(self.service_active)))

    def on_click_mode_comfort(self):
        self.driver.find_element(*self.service_comfort).click()

    """
        Phone number section
    """
    def on_click_phone_number(self):
       self.driver.find_element(*self.phone_field).click()

    def set_phone_number(self, phone_number):
        (WebDriverWait(self.driver,5)
         .until(expected_conditions.visibility_of_element_located(self.phone_input))).send_keys(phone_number)

    def on_click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def set_confirmation_code(self,code):
        (WebDriverWait(self.driver,5)
         .until(expected_conditions.visibility_of_element_located(self.code_input))).send_keys(code)

    def on_click_confirmation_button(self):
        self.driver.find_element(*self.confirm_button).click()