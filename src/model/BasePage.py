from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions

class BasePage:

    def __init__(self, driver):
        self.driver = driver


    # Espere hasta que el elemento sea visible
    def wait_element_visibility(self, element, timeout):
        return (WebDriverWait(self.driver, timeout)
                    .until(expected_conditions.visibility_of_element_located(element)))

    # Todos los elementos visibles
    def wait_elements_visibility(self, element, timeout):
        return (WebDriverWait(self.driver, timeout)
                    .until(expected_conditions.visibility_of_all_elements_located(element)))

    def wait_element_presence(self, element, timeout):
        return (WebDriverWait(self.driver, timeout)
                .until(expected_conditions.presence_of_element_located(element)))

    # Al menos un elemento presente
    def wait_elements_presence(self, element, timeout):
        return (WebDriverWait(self.driver, timeout)
                    .until(expected_conditions.presence_of_all_elements_located(element)))

    # Elemento clickable (visible + habilitado)
    def wait_clickable(self, element, timeout):
        return (WebDriverWait(self.driver, timeout)
                    .until(expected_conditions.element_to_be_clickable(element)))
