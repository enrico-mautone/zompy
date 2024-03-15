from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from zompy.steps.step import Step
from datetime import datetime, timedelta
import random
from zompy.steps.tap import Tap

class Behaviour(Step):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.steps = []
        self.driver = None
        self.context = {}

        if 'browser' in self.params:
            browser = self.params['browser']
            self.setup(browser, self.params['headless'])
     

    def setup(self, browser="Chrome", headless=False):
        if browser.lower() == "chrome":
            options = Options()
            if headless:
                options.add_argument("--headless")
            self.driver = webdriver.Chrome(options=options)
        return self
        

    def next(self, step: Step):
        self.steps.append(step)
        return self  # Consente la concatenazione in stile "fluid API"
    
    def next_tap(self,message:str,log_context=False):
        return self.next(Tap(message=message))\

    def execute(self,driver=None,context={}):
        if self.driver is None:
            self.driver = driver
            self.context = context
        for step in self.steps:
            try:
                step.execute(self.driver, self.context)  # Passa il contesto a ogni step
            except Exception as e:
                print(f"Exception caught during step execution: {e}")
                break  # Interrompe l'esecuzione in caso di eccezioni
        return self

    def quit(self):
        if self.driver:
            self.driver.quit()


def random_time_between(start_time_str, end_time_str):
    # Converte le stringhe iniziali e finali in oggetti datetime
    start_time = datetime.strptime(start_time_str, "%H:%M")
    end_time = datetime.strptime(end_time_str, "%H:%M")

    # Calcola la differenza tra i due orari
    delta = end_time - start_time

    # Genera un numero casuale di secondi all'interno dell'intervallo di tempo
    random_seconds = random.randint(0, delta.seconds)

    # Aggiunge il numero casuale di secondi all'orario di inizio per trovare un orario casuale nell'intervallo
    random_time = start_time + timedelta(seconds=random_seconds)

    # Converte l'orario casuale generato in una stringa nel formato desiderato
    return random_time.strftime("%H:%M")

def generate_today_date_string():
    # Ottiene l'oggetto datetime per la data di oggi
    today = datetime.today()
    
    # Formatta la data nel formato desiderato dd/mm/yyyy
    date_string = today.strftime("%d/%m/%Y")
    
    return date_string
