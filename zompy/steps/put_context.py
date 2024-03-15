from zompy.steps.step import Step


class Putcontext(Step):
    def execute(self, driver, context):
        if 'var' in self.params and 'value' in self.params:
             nome_var = self.params['var']
             value_var=  self.params['value']
             context[nome_var] = value_var