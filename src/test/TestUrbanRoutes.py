import time

from selenium import webdriver
from src.data import  Data
from src.config import Configuraton
from src.model.UrbanRoutesPage import UrbanRoutesPage
from src.utils.Retrive import retrieve_phone_code
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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


    # Configurar la dirección
    def test_set_route(self):

        from_field = (By.ID, 'from')
        to_field = (By.ID, 'to')

        address_from = Data.ADDRESS_FROM
        address_to = Data.ADDRESS_TO

        from_element = self.urban_routes.get_element(from_field)
        from_element.send_keys(address_from)

        to_element = self.urban_routes.get_element(to_field)
        to_element.send_keys(address_to)

        value_address_from = from_element.get_property('value')
        value_address_to = to_element.get_property('value')

        assert value_address_from == address_from
        assert value_address_to == address_to

    # Call taxi
    def test_selected_default_call_taxi(self):

        route_mode = (By.XPATH, '//div[@class="mode active" and text()="Flash"]')
        transport_mode = (By.XPATH, '//img[contains(@src, "taxi-active")]')
        call_taxi_button = (By.XPATH, '//button[@class="button round"]')

        mode_route_element = self.urban_routes.get_element(route_mode).text
        transport_element = self.urban_routes.get_element(transport_mode).get_attribute('src')
        call_element = self.urban_routes.get_element(call_taxi_button)

        assert mode_route_element == 'Flash' # check the default selected mode route
        assert 'taxi-active' in transport_element # check the default selected service fee

        call_element.click()

    # # Select the Comfort rate.
    def test_select_modo_comfort(self):

        service_active = (By.XPATH, '//div[@class="tcard active"]/div[@class="tcard-title"]')
        service_comfort = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')

        service_element = self.urban_routes.get_element(service_active).text# Laboral

        assert service_element == 'Laboral'# Check the selected default service mode

        comfort_element = self.urban_routes.get_element(service_comfort)
        comfort_element.click()

        new_selected_mode = self.urban_routes.get_element(service_active).text

        assert new_selected_mode == 'Comfort'# Check the selected comfort mode

    def test_fill_phone_number(self):

        phone_button = (By.CLASS_NAME, "np-text")
        phone_field = (By.ID, 'phone')
        next_button = (By.XPATH, '//button[@class="button full" and text()="Siguiente"]')
        code_field = (By.ID, 'code')
        confirm_button = (By.XPATH, '//button[@class="button full" and text()="Confirmar"]')

        phone_element = self.urban_routes.get_element(phone_button)
        phone_element.click()

        phone = Data.PHONE_NUMBER
        phone_element = self.urban_routes.get_element(phone_field)
        phone_element.send_keys(phone)

        value_phone = phone_element.get_property('value')

        assert value_phone == phone

        next_element = self.urban_routes.get_element(next_button)
        next_element.click()

        code = retrieve_phone_code(self.driver)
        code_element = self.urban_routes.get_element(code_field)
        code_element.send_keys(code)

        value_code = code_element.get_property('value')

        assert value_code == code# Check code phone value

        confirm_element = self.urban_routes.get_element(confirm_button)
        confirm_element.click()

    def test_payment_method(self):

        payment_method = (By.CLASS_NAME, 'pp-text')
        plus_button = (By.CLASS_NAME, 'pp-plus')
        card_number_input = (By.NAME, 'number')
        card_code_input = (By.NAME, 'code')
        add_card_button = (By.XPATH, '//button[@class="button full" and text()="Agregar"]')
        close_button = (By.XPATH, '//div[@class="section active"]/button[@class="close-button section-close"]')

        payment_element = self.urban_routes.get_element(payment_method)
        payment_element.click()

        plus_element = self.urban_routes.get_element(plus_button)
        plus_element.click()

        number = Data.CARD_NUMBER
        card_numer_element = self.urban_routes.get_element(card_number_input)
        card_numer_element.send_keys(number)
        value_number = card_numer_element.get_property('value')

        assert value_number == number

        cvv = Data.CARD_CODE
        cvv_element = self.urban_routes.get_element(card_code_input)
        cvv_element.send_keys(cvv)
        value_cvv = cvv_element.get_property('value')

        assert value_cvv == cvv

        cvv_element.send_keys(Keys.TAB)

        add_element = self.urban_routes.get_element(add_card_button)
        add_element.click()

        close_elements = self.urban_routes.get_elements(close_button)
        close_elements[1].click()
        time.sleep(5)

    @classmethod
    def teardown_class(cls):
        # cls.driver.delete_all_cookies()
        cls.driver.quit()
