from zompy.steps.step import Step
from selenium.webdriver.common.keys import Keys


class KeyboardInput(Step):
    def execute(self, driver,context):
        element = driver.find_element(self.params['by'], self.params['locator'])
        element = self.find_element(driver)
        text_to_type = self.params.get('text', '')
        
        # Se il testo da digitare include un segnaposto per il backspace, sostituirlo con Keys.BACK_SPACE
        if '[BKS]' in text_to_type:
            text_to_type = text_to_type.replace('[BKS]', Keys.BACK_SPACE)
        
        element.send_keys(text_to_type)