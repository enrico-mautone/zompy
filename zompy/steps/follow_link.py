from zompy.steps.step import Step


class FollowLink(Step):
    def execute(self, driver, context):
        # Determina il metodo di ricerca e il valore basato sui parametri forniti
        by_method = self.params.get('by')
        value = self.params.get('value')
        
        # Trova il link in base al metodo e al valore specificato e clicca su di esso
        link = driver.find_element(by_method, value)
        link.click()
