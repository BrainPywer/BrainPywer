"""
BrainPywer Events Implementation
"""
import inspect

class Events:
    def __init__(self):
        self._events = {}

    def add(self, func):
        """
        This is the decorator version of adding events
        :param func: The function we're registering as an event
        :return: func
        """
        setattr(self._events, func.__name__.lower(), func)
        return func

    def register(self, func):
        """
        This is a method for programatically adding new events
        :param func: The function we're registering as an event
        :return: func
        """
        setattr(self._events, func.__name__.lower(), func)
        return func

    def unregister(self, func):
        """
        This is a method for programatically removing events
        :param func: The function to remove
        :return: False if we failed to find the function to remove
        :return: True if we removed the function
        """
        if self._events.get(func.__name__.lower()) is None:
            return False
        else:
            self._events.pop(func.__name__.lower())
            return True

    def has_handler(self, event):
        """
        Do we have a handler defined for this event?
        :param event: The event name to handle
        :return: True if we have a handler defined
        :return: False if no handler is defined for the event
        """
        if self._events.get(event.lower()) is None:
            return False
        else:
            return True

    def dispatch(self, message):
        """
        This function takes a message received from the Dispatcher and sends it to the proper handler.
        If no handler is defined, we call the default handler which should always be defined.
        :param message: A tuple consisting of (event name, relavent data structure)
        :return: Nothing
        """
        if self._events.get(message[0].lower()) is None:
            self._events.get('default')(message[1])
        else:
            self._events.get(message[0].lower())(message[1])