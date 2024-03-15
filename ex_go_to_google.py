

from zompy.behaviour import Behaviour
from zompy.steps.navigate import Navigate


Behaviour().setup().next(Navigate(url="http://google.com")) \
    .execute()\
    .quit()