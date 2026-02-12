import time

from selenium import webdriver
from src.data import  Data
from src.data import Attributes
from src.config import Configuraton
from src.model.UrbanRoutesPage import UrbanRoutesPage
from src.utils.Retrive import retrieve_phone_code
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        # from selenium.webdriver import DesiredCapabilities
        # capabilities = DesiredCapabilities. CHROME
        # capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        options = Options()
        options.set_capability("goog:loggingPrefs",{"performance":"ALL"})
        cls.driver = webdriver.Chrome(service=Service(),options=options)
        cls.driver.get(Configuraton.URBAN_ROUTER_URL)
        cls.urban_routes = UrbanRoutesPage(cls.driver)


    # Configure the address
    def test_set_route(self):

        address_from = Data.ADDRESS_FROM
        address_to = Data.ADDRESS_TO

        from_element = self.urban_routes.get_element(Attributes.FROM_FIELD)
        from_element.send_keys(address_from)

        to_element = self.urban_routes.get_element(Attributes.TO_FIELD)
        to_element.send_keys(address_to)

        value_address_from = from_element.get_property('value')
        value_address_to = to_element.get_property('value')

        assert value_address_from == address_from
        assert value_address_to == address_to

    # Call a taxi
    def test_selected_default_call_taxi(self):

        mode_route_element = self.urban_routes.get_element(Attributes.ROUTE_MODE).text
        transport_element = self.urban_routes.get_element(Attributes.TRANSPORT_MODE).get_attribute('src')
        call_element = self.urban_routes.get_element(Attributes.CALL_TAXI_BUTTON)

        assert mode_route_element == 'Flash' # check the default selected mode route
        assert 'taxi-active' in transport_element # check the default selected service fee

        call_element.click()

    # Select the Comfort rate
    def test_select_modo_comfort(self):

        service_element = self.urban_routes.get_element(Attributes.SERVICE_ACTIVE).text# Laboral

        assert service_element == 'Laboral'# Check the selected default service mode

        comfort_element = self.urban_routes.get_element(Attributes.SERVICE_COMFORT)
        comfort_element.click()

        new_selected_mode = self.urban_routes.get_element(Attributes.SERVICE_ACTIVE).text

        assert new_selected_mode == 'Comfort'# Check the selected comfort mode

    # Fill in the phone number
    def test_fill_phone_number(self):

        phone_element = self.urban_routes.get_element(Attributes.PHONE_BUTTON)
        phone_element.click()

        phone = Data.PHONE_NUMBER
        phone_element = self.urban_routes.get_element(Attributes.PHONE_FIELD)
        phone_element.send_keys(phone)

        value_phone = phone_element.get_property('value')

        assert value_phone == phone

        next_element = self.urban_routes.get_element(Attributes.NEXT_BUTTON)
        next_element.click()

        code = retrieve_phone_code(self.driver)
        code_element = self.urban_routes.get_element(Attributes.CODE_FIELD)
        code_element.send_keys(code)

        value_code = code_element.get_property('value')

        assert value_code == code# Check code phone value

        confirm_element = self.urban_routes.get_element(Attributes.CONFIRM_BUTTON)
        confirm_element.click()

    # Add a credit card
    def test_payment_method(self):

        payment_element = self.urban_routes.get_element(Attributes.PAYMENT_METHOD_BUTTON)
        payment_element.click()

        plus_element = self.urban_routes.get_element(Attributes.PLUS_BUTTON)
        plus_element.click()

        number = Data.CARD_NUMBER
        card_numer_element = self.urban_routes.get_element(Attributes.CARD_NUMBER_INPUT)
        card_numer_element.send_keys(number)
        value_number = card_numer_element.get_property('value')

        assert value_number == number

        cvv = Data.CARD_CODE
        cvv_element = self.urban_routes.get_element(Attributes.CARD_CODE_INPUT)
        cvv_element.send_keys(cvv)
        value_cvv = cvv_element.get_property('value')

        assert value_cvv == cvv

        cvv_element.send_keys(Keys.TAB)

        add_element = self.urban_routes.get_element(Attributes.ADD_CARD_BUTTON)
        add_element.click()

        close_elements = self.urban_routes.get_elements(Attributes.CLOSE_BUTTON)
        close_elements[1].click()

    # Write a message for the controller
    def test_message_for_driver(self):

        message = Data.MESSAGE_FOR_DRIVER
        message_element = self.urban_routes.get_element(Attributes.MESSAGE_FIELD)
        message_element.send_keys(message)
        value_message = message_element.get_property('value')

        assert value_message == message

    # Ask for a blanket and handkerchiefs
    def test_for_blanket_and_handkerchiefs(self):

        slider_elements = self.urban_routes.get_elements(Attributes.BLANK_AND_HANDKERCHIEFS)

        slider_elements[0].click()

        assert slider_elements[0].is_selected() != True

    # Order 2 ice creams
    def test_order_2_ice_creams(self):

        plus_elements = self.urban_routes.get_elements(Attributes.ICE_CREAMS_PLUS)

        for cnt in range(2):
            plus_elements[0].click()

        cnt_elements = self.urban_routes.get_elements(Attributes.ICE_CREAMS_CNT)
        cnt  = cnt_elements[0].text

        assert cnt == '2'

    @classmethod
    def teardown_class(cls):
        # cls.driver.delete_all_cookies()
        cls.driver.quit()
