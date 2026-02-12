from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, element):
        return (WebDriverWait(self.driver,5)
                .until(EC.visibility_of_element_located(element)))


    def get_elements(self, element):
        return (WebDriverWait(self.driver,5)
                .until(EC.presence_of_all_elements_located(element)))