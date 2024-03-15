from zompy.steps.step import Step


class ButtonPress(Step):
    def execute(self, driver, context):
        # Esempio di utilizzo del contesto per trovare un elemento salvato da uno step precedente
        if 'button' in context:
            button = context['button']
            button.click()
        else:
            button = self.find_element(driver)
            button.click()
