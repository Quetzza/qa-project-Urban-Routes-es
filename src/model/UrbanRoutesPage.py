from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions
from src.model.BasePage import BasePage
import time




class UrbanRoutesPage(BasePage):

    FROM_FIELD = (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')
    # ADDRESS_FIELD = (By.XPATH,  '//div[@class="input-container"]/input[@class="input"]')

    ROUTE_MODE = (By.XPATH, '//div[@class="mode active" and text()="Flash"]')
    TRANSPORT_MODE = (By.XPATH, '//img[contains(@src, "taxi-active")]')
    CALL_SERVICE_BUTTON = (By.XPATH, '//button[@class="button round"]')

    SERVICE_ACTIVE = (By.XPATH, '//div[@class="tcard active"]/div[@class="tcard-title"]')
    SERVICE_COMFORT = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')

    PHONE_BUTTON = (By.CLASS_NAME, "np-text")
    PHONE_FIELD = (By.ID, 'phone')
    NEXT_BUTTON = (By.XPATH, '//button[@class="button full" and text()="Siguiente"]')
    PHONE_CODE_FIELD = (By.ID, 'code')
    CONFIRM_BUTTON = (By.XPATH, '//button[@class="button full" and text()="Confirmar"]')

    PAYMENT_METHOD_BUTTON = (By.CLASS_NAME, 'pp-text')
    PLUS_BUTTON = (By.CLASS_NAME, 'pp-plus')
    CARD_NUMBER_FIELD = (By.ID, 'number')
    CARD_CODE_FIELD = (By.NAME, 'code')
    CARD_FIELDS = (By.XPATH, '//div[@class="card-wrapper"]//input[@class="card-input"]')
    ADD_CARD_BUTTON = (By.XPATH, '//button[@class="button full" and text()="Agregar"]')
    CLOSE_BUTTON = (By.XPATH, '//div[@class="section active"]/button[@class="close-button section-close"]')
    
    MESSAGE_FIELD = (By.ID, 'comment')


    CHECKED_INPUT = (By.XPATH, '//input[@class="switch-input"]')
    BLANK_AND_HANDKERCHIEFS_SLIDER = (By.XPATH, '//span[@class="slider round"]')
    
    ICE_CREAMS_PLUS = (By.XPATH, '//div[@class="counter-plus"]')
    ICE_CREAMS_CNT = (By.XPATH, '//div[@class="counter-value"]')

    SMART_BUTTON = (By.XPATH, '//span[@class="smart-button-main"]')
    ORDER_TIME = (By.CLASS_NAME, 'order-header-time')
    MODAL_BUTTONS = (By.XPATH, '//div[@class="order-btn-group"]')

    def __init__(self, driver):
        super().__init__(driver)

    def get_from(self):
        return self.wait_element_presence(self.FROM_FIELD, 5).get_property('value')

    def get_to(self):
        return self.wait_element_presence(self.TO_FIELD, 5).get_property('value')

    def set_route(self, address_from, address_to):
       self.wait_element_visibility(self.FROM_FIELD,5).send_keys(address_from)
       self.wait_element_visibility(self.TO_FIELD,5).send_keys(address_to)

    def get_service(self):
        return self.wait_element_visibility(self.SERVICE_ACTIVE,5).text

    def select_mode_comfort(self):

        self.wait_clickable(self.CALL_SERVICE_BUTTON,5).click()
        self.wait_clickable(self.SERVICE_COMFORT,5).click()

    def get_phone_number(self):
        return self.wait_element_presence(self.PHONE_FIELD,5).get_property('value')

    def get_phone_code(self):
        return self.wait_element_presence(self.PHONE_CODE_FIELD,5).get_property('value')

    def add_phone_number(self, phone_number):

        self.wait_clickable(self.PHONE_BUTTON,5).click()

        self.wait_element_visibility(self.PHONE_FIELD,5).send_keys(phone_number)

        self.wait_clickable(self.NEXT_BUTTON,5).click()

    def add_phone_code(self, code):
        self.wait_element_visibility(self.PHONE_CODE_FIELD, 5).send_keys(code)

        self.wait_clickable(self.CONFIRM_BUTTON,5).click()

    def get_card_number(self):
        return self.wait_element_presence(self.CARD_NUMBER_FIELD,5).get_property('value')

    def get_card_code(self):
        return self.wait_element_presence(self.CARD_CODE_FIELD,5).get_property('value')

    def add_credit_card(self, number, code):

        self.wait_clickable(self.PAYMENT_METHOD_BUTTON,5).click()
        self.wait_clickable(self.PLUS_BUTTON,5).click()

        self.wait_element_visibility(self.CARD_NUMBER_FIELD,5).send_keys(number)# card number
        self.wait_element_visibility(self.CARD_CODE_FIELD,5).send_keys(code) # card code

        self.wait_element_visibility(self.CARD_CODE_FIELD,5).send_keys(Keys.TAB)# Change focus

        self.wait_clickable(self.ADD_CARD_BUTTON,5).click()
        self.wait_elements_presence(self.CLOSE_BUTTON,5)[1].click()

    def get_message_for_driver(self):
        return self.wait_element_presence(self.MESSAGE_FIELD,5).get_property('value')

    def add_message_for_driver(self, message):

        self.wait_element_visibility(self.MESSAGE_FIELD,5).send_keys(message)

    def get_checked_blanket_and_handkerchiefs(self):
        return self.wait_elements_presence(self.CHECKED_INPUT,5)[0].get_property('checked')

    def add_blanket_and_handkerchiefs(self):

        self.wait_elements_presence(self.BLANK_AND_HANDKERCHIEFS_SLIDER,5)[0].click()

    def get_count_ice_creams(self):
        return self.wait_elements_visibility(self.ICE_CREAMS_CNT,5)[0].text

    def add_two_ice_creams(self):

        for cnt in range(2):
            self.wait_elements_visibility(self.ICE_CREAMS_PLUS, 5)[0].click()

    def call_taxi(self):

        self.wait_clickable(self.SMART_BUTTON,5).click()

        elements = self.__get_elements_visibility(self.MODAL_BUTTONS,5)

        assert len(elements) == 2

        time.sleep(1)

        timer = self.__get_element_visibility(self.ORDER_TIME,5).text

        m, s = map(int, timer.split(':'))

        time.sleep(s)

        elements = self.__get_elements_presence(self.MODAL_BUTTONS, 5)

        assert len(elements) == 3