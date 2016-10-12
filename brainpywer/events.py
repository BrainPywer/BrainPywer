"""
BrainPywer Events Implementation
Some implementation details taken from discord.py written by Danny/Rapptz at https://github.com/Rapptz/discord.py
"""
import inspect

class Events:
    """

    """
    def __init__(self):
        self._events = {}

    def add(self, func):
        """
        This is the decorator version of adding events

        :param func: The function we're registering as an event
        :type func: function
        :return: func
        """
        setattr(self, func.__name__, func)
        self._events[func.__name__.lower()] = getattr(self, func.__name__)
        return func

    def register(self, func):
        """
        This is a method for programatically adding new events

        :param func: The function we're registering as an event
        :type func: function
        :return: func
        """
        setattr(self, func.__name__, func)
        self._events[func.__name__.lower()] = getattr(self, func.__name__)
        return func

    def unregister(self, func):
        """
        This is a method for programatically removing events

        :param func: The name of the event to unregister
        :type func: function
        :return: False if we failed to find the function to remove
        :return: True if we removed the function
        """
        if self._events.get(func.lower()) is None:
            return False
        else:
            delattr(self, self._events[func.lower()].__name__)
            self._events.pop(func.lower())
            return True

    def has_handler(self, event):
        """
        Do we have a handler defined for this event?

        :param event: The event name to handle
        :type event: str
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

        :param message: The message to be dispatched.
        :type message: tuple (event name, relevant data)
        :return: Nothing
        """
        if self._events.get(message[0].lower()) is None:
            self._events.get('default')(message[1])
        else:
            self._events.get(message[0].lower())(message[1])