

from zompy.behaviour import Behaviour
from zompy.steps.navigate import Navigate
from zompy.steps.wait import Wait


Behaviour().setup().next(Navigate(url="http://gamedev.net")) \
    .next(Wait(random_time=10))\
    .execute()\
    .quit()