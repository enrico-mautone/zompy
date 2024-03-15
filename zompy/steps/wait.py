import time
from random import randint
from zompy.steps.step import Step
from selenium.webdriver.support.ui import WebDriverWait

class Wait(Step):
    def execute(self, driver, context):
        # Controlla se è stato fornito un tempo massimo di attesa random
        if 'random_time' in self.params:
            max_time = self.params['random_time']
            time_to_wait = randint(1, max_time)  # Seleziona un tempo casuale tra 1 e random_time
            time.sleep(time_to_wait)
        # Controlla se è stata fornita una condizione di attesa
        elif 'condition' in self.params and 'timeout' in self.params:
            condition = self.params['condition']
            timeout = self.params['timeout']
            button = WebDriverWait(driver, timeout).until(condition)
            context['button'] = button
        else:
            # Se non è specificata nessuna delle opzioni sopra, attende un tempo predefinito
            time_to_wait = self.params.get('seconds', 1)  # Predefinito a 1 secondo se non specificato
            time.sleep(time_to_wait)
