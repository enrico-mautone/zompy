from zompy.steps.step import Step


class Tap(Step):
    def execute(self, driver, context):
        # Estrae il messaggio dai parametri
        message = self.params.get('message', '')
        print(f"{message}")

        # Se log_context è True, stampa anche il contesto
        if self.params.get('log_context', False):
            print("Context:", context)
