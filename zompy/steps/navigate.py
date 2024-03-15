from zompy.steps.step import Step


class Navigate(Step):
    def execute(self, driver, context):
        driver.get(self.params['url'])