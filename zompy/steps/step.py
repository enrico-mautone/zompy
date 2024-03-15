from abc import ABC, abstractmethod
from selenium.webdriver.common.by import By

class Step(ABC):
    def __init__(self,**kwargs):
        self.params = kwargs

    @abstractmethod
    def execute(self, driver, context):
        pass
             

    def find_element(self, driver):
        # Ricerca l'elemento sulla pagina utilizzando i parametri forniti
        return driver.find_element(self.params['by'], self.params['locator'])


