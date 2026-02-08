from selenium import webdriver
from ..data import  data
from ..config import configuraton
from ..model.FromToPageUrbanRoutes import FromToPageUrbanRoutes
class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        # from selenium.webdriver import DesiredCapabilities
        # capabilities = DesiredCapabilities. CHROME
        # capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.get(configuraton.URBAN_ROUTER_URL)

    def test_set_route(self):
        routes_page = FromToPageUrbanRoutes(self.driver)
        address_from = data.ADDRESS_FROM # 'East 2nd Street, 601'
        address_to = data.ADDRESS_TO # '1300 1st St'
        routes_page.wait_for_load_address_field() # wait 5s
        routes_page.set_route(address_from, address_to)# write address on fields
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
