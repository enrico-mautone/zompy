from datetime import datetime
from croniter import croniter
import time
import threading

class Bot:
    def __init__(self):
        self.behaviours = {}

    def add_behaviour(self, name, behaviour, cron_string, repeat=-1):
        if name in self.behaviours:
            raise ValueError(f"Un Behaviour con il nome {name} è già stato aggiunto.")
        
        # Salva il Behaviour con la sua cron string e il contatore di ripetizione
        self.behaviours[name] = {'behaviour': behaviour, 'cron': cron_string, 'repeat': repeat}

    def execute_behaviour(self, name):
        behaviour_info = self.behaviours[name]
        behaviour = behaviour_info['behaviour']
        print(f"Esecuzione del Behaviour {name} a {datetime.now()}")
        behaviour.execute()
        
        # Decrementa il contatore se necessario
        if behaviour_info['repeat'] > 0:
            behaviour_info['repeat'] -= 1
            if behaviour_info['repeat'] == 0:
                self.remove_behaviour(name)

    def remove_behaviour(self, name):
        if name in self.behaviours:
            del self.behaviours[name]
            print(f"Behaviour {name} rimosso.")

    def start(self):
        for name, info in self.behaviours.items():
            cron = croniter(info['cron'], datetime.now())
            next_time = cron.get_next(datetime)
            
            # Calcola il tempo di attesa in secondi
            wait_time = (next_time - datetime.now()).total_seconds()
            
            if info['repeat'] != 0:  # 0 indica che il Behaviour è stato disattivato
                threading.Timer(wait_time, self.execute_behaviour, args=(name,)).start()

# Esempio di utilizzo
# if __name__ == "__main__":
#     bot = Bot()
#     # Aggiungi qui i tuoi Behaviour con i relativi nomi, oggetti Behaviour, stringhe cron e ripetizioni
#     # bot.add_behaviour("nome_behaviour", behaviour_obj, "* * * * *", repeat=-1)  # Esempio di cron string per ogni minuto

#     bot.start()
