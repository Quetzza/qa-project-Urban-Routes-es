from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import time

class UrbanRoutesPage:

    FROM_FIELD = (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')

    ROUTE_MODE = (By.XPATH, '//div[@class="mode active" and text()="Flash"]')
    TRANSPORT_MODE = (By.XPATH, '//img[contains(@src, "taxi-active")]')
    CALL_TAXI_BUTTON = (By.XPATH, '//button[@class="button round"]')

    SERVICE_ACTIVE = (By.XPATH, '//div[@class="tcard active"]/div[@class="tcard-title"]')
    SERVICE_COMFORT = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')

    PHONE_BUTTON = (By.CLASS_NAME, "np-text")
    PHONE_FIELD = (By.ID, 'phone')
    NEXT_BUTTON = (By.XPATH, '//button[@class="button full" and text()="Siguiente"]')
    CODE_FIELD = (By.ID, 'code')
    CONFIRM_BUTTON = (By.XPATH, '//button[@class="button full" and text()="Confirmar"]')

    PAYMENT_METHOD_BUTTON = (By.CLASS_NAME, 'pp-text')
    PLUS_BUTTON = (By.CLASS_NAME, 'pp-plus')
    CARD_NUMBER_INPUT = (By.NAME, 'number')
    CARD_CODE_INPUT = (By.NAME, 'code')
    ADD_CARD_BUTTON = (By.XPATH, '//button[@class="button full" and text()="Agregar"]')
    CLOSE_BUTTON = (By.XPATH, '//div[@class="section active"]/button[@class="close-button section-close"]')
    
    MESSAGE_FIELD = (By.ID, 'comment')
    
    BLANK_AND_HANDKERCHIEFS_INPUT = (By.XPATH, '//input[@class="switch-input"]')
    BLANK_AND_HANDKERCHIEFS_SLIDER = (By.XPATH, '//span[@class="slider round"]')
    
    ICE_CREAMS_PLUS = (By.XPATH, '//div[@class="counter-plus"]')
    ICE_CREAMS_CNT = (By.XPATH, '//div[@class="counter-value"]')

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(self.driver,5)

    def __get_visibility_element(self, element):
        return self.wait.until(EC.visibility_of_element_located(element))

    def __get_visibility_elements(self, element):
        return self.wait.until(EC.visibility_of_all_elements_located(element))

    def __get_fiend_elements(self, element):
        return self.driver.find_elements(*element)
    
    def __get_presence_elements(self, element):
        return self.wait.until(EC.presence_of_all_elements_located(element))
    
    def __get_clickable_element(self, element):
        return self.wait.until(EC.element_to_be_clickable(element))

        

    def set_route(self, address_from, address_to):

        from_element = self.__get_visibility_element(self.FROM_FIELD)
        from_element.send_keys(address_from)
       
        to_element = self.__get_visibility_element(self.TO_FIELD)
        to_element.send_keys(address_to)

        value_from_element = from_element.get_property('value')
        value_to_element   = to_element.get_property('value')

        assert value_from_element == address_from
        assert value_to_element == address_to

    def __call_service_taxi(self):

        mode_route_element = self.__get_visibility_element(self.ROUTE_MODE)
        mode_route = mode_route_element.text

        transport_element = self.__get_visibility_element(self.TRANSPORT_MODE)
        transport = transport_element.get_attribute('src')

        assert mode_route == 'Flash'
        assert 'taxi-active' in transport

        call_service_taxi_button = self.__get_clickable_element(self.CALL_TAXI_BUTTON)
        call_service_taxi_button.click()

    def select_mode_comfort(self):

        self.__call_service_taxi()

        service_element = self.__get_visibility_element(self.SERVICE_ACTIVE)
        current_service = service_element.text

        assert current_service == 'Laboral'

        service_comfort = self.__get_clickable_element(self.SERVICE_COMFORT)
        service_comfort.click()

        new_selected_service= self.__get_visibility_element(self.SERVICE_ACTIVE)
        new_current_service = new_selected_service.text

        assert new_current_service == 'Comfort'
    
    def __clickable_phone_number(self):

        phone_number_element = self.__get_clickable_element(self.PHONE_BUTTON)
        phone_number_element.click()
    
    def __clickable_next_button(self):
        
        next_element = self.__get_clickable_element(self.NEXT_BUTTON)
        next_element.click()

    def __clickable_confirm_button(self):

        confirm_element = self.__get_clickable_element(self.CONFIRM_BUTTON)
        confirm_element.click()

    def __set_phone_number(self, phone_number):

        phone_number_element = self.__get_visibility_element(self.PHONE_FIELD)
        phone_number_element.send_keys(phone_number)

        value_phone_number = phone_number_element.get_property('value')

        assert value_phone_number == phone_number
    
    def __set_phone_code(self, code):
        
        code_element = self.__get_visibility_element(self.CODE_FIELD)
        code_element.send_keys(code)

        value_code = code_element.get_property('value')

        assert value_code == code

    def add_phone_number(self, phone_number):
        self.__clickable_phone_number()
        self.__set_phone_number(phone_number)
        self.__clickable_next_button()

    def add_phone_code(self, code):
        self.__set_phone_code(code)
        self.__clickable_confirm_button()    
    
    def __clickable_payment_method(self):
        payment_method_element = self.__get_visibility_element(self.PAYMENT_METHOD_BUTTON)
        payment_method_element.click()
    
    def __clickable_plus_button(self):
        plus_button_element = self.__get_clickable_element(self.PLUS_BUTTON)
        plus_button_element.click()
    
    def __clickable_add_card(self):
        add_element = self.__get_clickable_element(self.ADD_CARD_BUTTON)
        add_element.click()
    
    def __clickable_close_payment_method(self):
        close_element = self.__get_presence_elements(self.CLOSE_BUTTON)
        close_element[1].click()

    def __set_card_number(self, card_number):

        card_number_element = self.__get_visibility_element(self.CARD_NUMBER_INPUT)
        card_number_element.send_keys(card_number)
        
        value_card_number = card_number_element.get_property('value')

        assert value_card_number == card_number
    
    def __set_card_code(self, card_code):

        card_code_element = self.__get_visibility_element(self.CARD_CODE_INPUT)
        card_code_element.send_keys(card_code)
        
        value_card_number = card_code_element.get_property('value')

        assert value_card_number == card_code

        card_code_element.send_keys(Keys.TAB)

    def add_credit_card(self, card_number, card_code):

        self.__clickable_payment_method()
        self.__clickable_plus_button()
        self.__set_card_number(card_number)
        self.__set_card_code(card_code)
        self.__clickable_add_card()
        self.__clickable_close_payment_method()
    
    def __set_message(self, message):

        message_element = self.__get_visibility_element(self.MESSAGE_FIELD)
        message_element.send_keys(message)

        value_message = message_element.get_property('value')

        assert value_message == message
    
    def add_message_for_driver(self, message):
        
        self.__set_message(message)
    
    def add_blanket_and_handkerchiefs(self):

        input_element = self.__get_fiend_elements(self.BLANK_AND_HANDKERCHIEFS_INPUT)

        slider_element = self.__get_presence_elements(self.BLANK_AND_HANDKERCHIEFS_SLIDER)
        slider_element[0].click()

        current_checked = input_element[0].get_property('checked')

        assert  current_checked == True

    def add_two_ice_creams(self):
        
        plus_element = self.__get_presence_elements(self.ICE_CREAMS_PLUS)

        for cnt in range(2):
            plus_element[0].click()
        
        cnt_element = self.__get_presence_elements(self.ICE_CREAMS_CNT)
        cnt_ice_creams = cnt_element[0].text

        assert cnt_ice_creams == '2' 