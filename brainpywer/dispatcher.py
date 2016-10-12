"""
BrainPywer Dispatcher
Purpose: The Dispatcher handles communication between the Interface and Gateway
"""
import gevent
from gevent.queue import JoinableQueue, Empty


class Dispatcher(gevent.Greenlet):
    """
    The Dispatcher class handles routing communications to and from the Gateway.
    It implements an Actor interface as made popular by Erlang.
    """

    def __init__(self):
        self._gw_inbox = JoinableQueue()
        super().__init__()

    def _run(self):
        while True:
            try:
                event = self._gw_inbox.get(block=False)
                # Dispatch the event back to interface
                self._gw_inbox.task_done()
            finally:
                gevent.sleep(1)

    @property
    def gw_inbox(self):
        """
        This is the inbox for the Gateway. It's not accesible outside the class methods.

        :return: None
        """
        return None

    @gw_inbox.setter
    def gw_inbox(self, message):
        self._gw_inbox.put(message)
