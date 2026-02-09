from selenium import webdriver
from src.data import  Data
from src.config import Configuraton
from src.model.FromToPageUrbanRoutes import FromToPageUrbanRoutes
from src.model.CallTaxiPage import CallTaxiPage
from src.model.ModeComfortPage import ModeComfortPage
class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        # from selenium.webdriver import DesiredCapabilities
        # capabilities = DesiredCapabilities. CHROME
        # capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.get(Configuraton.URBAN_ROUTER_URL)


    # Configurar la dirección
    def test_set_route(self):
        routes_page = FromToPageUrbanRoutes(self.driver)
        address_from = Data.ADDRESS_FROM # 'East 2nd Street, 601'
        address_to = Data.ADDRESS_TO # '1300 1st St'
        routes_page.wait_for_load_address_field() # wait 5s
        routes_page.set_route(address_from, address_to)# write address on fields
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    # Call taxi
    def test_call_taxi(self):
        taxi_page = CallTaxiPage(self.driver)
        taxi_page.call_taxi()

    #Seleccionar la tarifa Comfort.
    def test_on_clic_call_taxi_comfort(self):
        comfort = ModeComfortPage(self.driver)
        comfort.set_mode_comfort()

    @classmethod
    def teardown_class(cls):
        # cls.driver.delete_all_cookies()
        cls.driver.quit()
