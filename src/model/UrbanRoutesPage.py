from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions
import time

class UrbanRoutesPage:

    ADDRESS_FIELD = (By.XPATH,  '//div[@class="input-container"]/input[@class="input"]')

    ROUTE_MODE = (By.XPATH, '//div[@class="mode active" and text()="Flash"]')
    TRANSPORT_MODE = (By.XPATH, '//img[contains(@src, "taxi-active")]')
    CALL_SERVICE_BUTTON = (By.XPATH, '//button[@class="button round"]')

    SERVICE_ACTIVE = (By.XPATH, '//div[@class="tcard active"]/div[@class="tcard-title"]')
    SERVICE_COMFORT = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')

    PHONE_BUTTON = (By.CLASS_NAME, "np-text")
    PHONE_FIELD = (By.ID, 'phone')
    NEXT_BUTTON = (By.XPATH, '//button[@class="button full" and text()="Siguiente"]')
    CODE_FIELD = (By.ID, 'code')
    CONFIRM_BUTTON = (By.XPATH, '//button[@class="button full" and text()="Confirmar"]')

    PAYMENT_METHOD_BUTTON = (By.CLASS_NAME, 'pp-text')
    PLUS_BUTTON = (By.CLASS_NAME, 'pp-plus')
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
        self.driver = driver

    # Espere hasta que el elemento sea visible
    def __get_element_visibility(self, element, timeout):
        return (WebDriverWait(self.driver, timeout)
                .until(expected_conditions.visibility_of_element_located(element)))

    # Todos los elementos visibles
    def __get_elements_visibility(self, element,timeout):
        return (WebDriverWait(self.driver, timeout)
                .until(expected_conditions.visibility_of_all_elements_located(element)))

    # Al menos un elemento presente
    def __get_elements_presence(self, element, timeout):
        return (WebDriverWait(self.driver, timeout)
                .until(expected_conditions.presence_of_all_elements_located(element)))

    # Elemento clickable (visible + habilitado)
    def __get_element_clickable(self, element, timeout):
        return (WebDriverWait(self.driver, timeout)
                .until(expected_conditions.element_to_be_clickable(element)))



    def set_route(self, address_from, address_to):

        elements = self.__get_elements_visibility(self.ADDRESS_FIELD,5)

        elements[0].send_keys(address_from)# from input
        elements[1].send_keys(address_to)# to input

        assert elements[0].get_property('value') == address_from
        assert elements[1].get_property('value') == address_to

    def select_mode_comfort(self):

        self.__get_element_clickable(self.CALL_SERVICE_BUTTON,5).click()
        self.__get_element_clickable(self.SERVICE_COMFORT,5).click()

        current_service = self.__get_element_visibility(self.SERVICE_ACTIVE,5).text

        assert current_service == 'Comfort'

    def add_phone_number(self, phone_number):

        self.__get_element_clickable(self.PHONE_BUTTON,5).click()

        element = self.__get_element_visibility(self.PHONE_FIELD,5)
        element.send_keys(phone_number)

        assert element.get_property('value') == phone_number

        self.__get_element_clickable(self.NEXT_BUTTON,5).click()

    def add_phone_code(self, code):

        element = self.__get_element_visibility(self.CODE_FIELD,5)
        element.send_keys(code)

        assert  element.get_property('value') == code

        self.__get_element_clickable(self.CONFIRM_BUTTON,5).click()

    def add_credit_card(self, card_number, card_code):

        self.__get_element_clickable(self.PAYMENT_METHOD_BUTTON,5).click()
        self.__get_element_clickable(self.PLUS_BUTTON,5).click()

        elements = self.__get_elements_visibility(self.CARD_FIELDS,5)

        elements[0].send_keys(card_number) # card number
        elements[1].send_keys(card_code) # card code

        assert elements[0].get_property('value') == card_number
        assert elements[1].get_property('value') == card_code

        elements[1].send_keys(Keys.TAB)# Change focus

        self.__get_element_clickable(self.ADD_CARD_BUTTON,5).click()
        self.__get_elements_presence(self.CLOSE_BUTTON,5)[1].click()
    
    def add_message_for_driver(self, message):

        message_element = self.__get_element_visibility(self.MESSAGE_FIELD,5)
        message_element.send_keys(message)

        assert  message_element.get_property('value') == message

    def add_blanket_and_handkerchiefs(self):

        checked_elements = self.__get_elements_presence(self.CHECKED_INPUT,5)

        self.__get_elements_presence(self.BLANK_AND_HANDKERCHIEFS_SLIDER,5)[0].click()

        assert checked_elements[0].get_property('checked') == True

    def add_two_ice_creams(self):

        for cnt in range(2):
            self.__get_elements_visibility(self.ICE_CREAMS_PLUS, 5)[0].click()

        cnt_element = self.__get_elements_visibility(self.ICE_CREAMS_CNT,5)[0].text

        assert cnt_element == '2'

    def call_taxi(self):

        self.__get_element_clickable(self.SMART_BUTTON,5).click()

        elements = self.__get_elements_visibility(self.MODAL_BUTTONS,5)

        assert len(elements) == 2

        time.sleep(1)

        timer = self.__get_element_visibility(self.ORDER_TIME,5).text

        m, s = map(int, timer.split(':'))

        time.sleep(s)

        elements = self.__get_elements_presence(self.MODAL_BUTTONS, 5)

        assert len(elements) == 3