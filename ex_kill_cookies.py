

from zompy.behaviour import Behaviour
from zompy.steps.put_context import Putcontext
from zompy.steps.button_press import ButtonPress
from zompy.steps.navigate import Navigate
from zompy.steps.tap import Tap
from zompy.steps.wait import Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located



Behaviour().setup().next(Navigate(url="https://google.com")) \
    .next(Wait(timeout=10,condition=presence_of_element_located((
        By.XPATH,
        "/html/body/div[2]/div[3]/div[3]/span/div/div/div/div[3]/div[1]/button[2]"))))\
    .next(ButtonPress())\
    .next(Putcontext(var='mia_var',value=34))\
    .next(Tap(message="Cookies andati!",log_context=True))\
    .next(Wait(seconds=5))\
    .next(Tap(message="Prima di fine."))\
    .next_tap("Fine.")\
    .execute()\
    .quit()


# .next(Wait(timeout=10,condition=presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[3]/span/div/div/div/div[3]/div[1]/button[2]")))\