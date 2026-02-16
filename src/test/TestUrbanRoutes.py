import time

from src.data import  Data
from src.config import Configuration
from src.model.UrbanRoutesPage import UrbanRoutesPage
from src.utils.Retrieve import retrieve_phone_code
from selenium import webdriver
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
        cls.driver.get(Configuration.URBAN_ROUTER_URL)
        cls.urban_routes = UrbanRoutesPage(cls.driver)


    # Configure the address
    def test_set_route(self):

        address_from = Data.ADDRESS_FROM
        address_to = Data.ADDRESS_TO

        self.urban_routes.set_route(address_from, address_to)

    # Select the Comfort rate
    def test_select_modo_comfort(self):

        self.urban_routes.select_mode_comfort()

    # Fill in the phone number
    def test_fill_phone_number(self):

        phone_number = Data.PHONE_NUMBER

        self.urban_routes.add_phone_number(phone_number)

        code = retrieve_phone_code(self.driver)

        self.urban_routes.add_phone_code(code)

    # Add a credit card
    def test_add_payment_method(self):

        card_number = Data.CARD_NUMBER
        card_code   = Data.CARD_CODE

        self.urban_routes.add_credit_card(card_number, card_code)

    # Write a message for the controller
    def test_message_for_driver(self):

        message = Data.MESSAGE_FOR_DRIVER

        self.urban_routes.add_message_for_driver(message)

    # Ask for a blanket and handkerchiefs
    def test_for_blanket_and_handkerchiefs(self):

        self.urban_routes.add_blanket_and_handkerchiefs()

    # Order 2 ice creams
    def test_order_2_ice_creams(self):

       self.urban_routes.add_two_ice_creams()

    def test_call_taxi(self):

        self.urban_routes.call_taxi()

    @classmethod
    def teardown_class(cls):
        # cls.driver.delete_all_cookies()
        cls.driver.quit()
