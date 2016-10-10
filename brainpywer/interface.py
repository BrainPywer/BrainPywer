"""
BrainPywer Interface
Purpose: The Interface is the forward facing API that the programmer interacts with
"""
import gevent
from gevent.event import Event
from .events import Events


class Interface(Events):
    def __init__(self):
        super().__init__()


