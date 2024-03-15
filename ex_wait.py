

from zompy.behaviour import Behaviour
from zompy.steps.navigate import Navigate
from zompy.steps.wait import Wait


Behaviour().setup().next(Navigate(url="http://gamedev.net")) \
    .next(Wait(seconds=10))\
    .execute()\
    .quit()