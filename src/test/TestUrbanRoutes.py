from selenium import webdriver
from src.data import  Data
from src.config import Configuraton
from src.model.UrbanRoutesPage import UrbanRoutesPage
from src.utils.Retrive import retrieve_phone_code
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
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


    # Configurar la dirección
    def test_set_route(self):
        routes_page = UrbanRoutesPage(self.driver)
        address_from = Data.ADDRESS_FROM # 'East 2nd Street, 601'
        address_to = Data.ADDRESS_TO # '1300 1st St'
        routes_page.set_route(address_from, address_to)# write address on fields
        assert routes_page.get_from_value() == address_from
        assert routes_page.get_to_value() == address_to

    # Call taxi
    def test_selected_default_call_taxi(self):
        selected_default = UrbanRoutesPage(self.driver)
        mode_route = selected_default.get_default_mode_route().text # Flash
        transport = selected_default.get_default_transport() # "/static/media/taxi-active.b0be3054.svg"
        assert mode_route == 'Flash' # check the default selected mode route
        assert 'taxi-active' in transport # check the default selected service fee
        selected_default.call_taxi()

    # # Select the Comfort rate.
    def test_set_mode_comfort(self):
        mode_comfort = UrbanRoutesPage(self.driver)
        mode_comfort.set_mode_comfort()
        new_service_selected = mode_comfort.get_service_mode()
        assert new_service_selected.text == 'Comfort'# Check the selected comfort mode

    def test_fill_phone_number(self):
        phone_page = UrbanRoutesPage(self.driver)
        phone_page.fill_phone_number(Data.PHONE_NUMBER)
        code = retrieve_phone_code(self.driver)
        phone_page.set_confirmation_code(code)
        assert phone_page.get_code_value() == code  # check code phone value
        phone_page.fill_confirmation_code()


    @classmethod
    def teardown_class(cls):
        cls.driver.delete_all_cookies()
        cls.driver.quit()
