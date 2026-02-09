from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class CallTaxiComfortPage:

    route_mode = (By.XPATH, '//div[@class="mode active" and text()="Flash"]')
    service_fee = (By.XPATH, '//div[@class="type active disabled"]/img[@class="type-icon"]')
    call_taxi_button = (By.XPATH, '//button[@class="button round"]')

    def __init__(self, drive):
        self.driver = drive
    #Optimo - Flash - Personal
    def get_default_mode_route(self):
        return self.driver.find_element(*self.route_mode).text
    # car - walk - taxi - bike - scooter - drive
    def get_default_service_fee(self):
        return self.driver.find_element(*self.service_fee).get_attribute('src')

    def on_click_call_taxi_button(self):
        (WebDriverWait(self.driver,5)
         .until(expected_conditions
                .visibility_of_element_located(self.call_taxi_button))).click()