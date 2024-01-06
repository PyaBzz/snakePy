import unittest
from unittest.mock import MagicMock
from source.event import Event
from source.event_hub import EventHub


class Worm_(unittest.IsolatedAsyncioTestCase):
    _msec = 0.001
    _some_number_1 = 7
    _some_number_2 = 10

    def __init__(self, *args, **kwargs):
        super(Worm_, self).__init__(*args, **kwargs)

        self._events = EventHub()

        self._events.stepped = Event()
        self.stepped_callback = MagicMock()
        self._events.stepped.subscribe(self.stepped_callback)

        self._events.ate = Event()
        self.ate_callback = MagicMock()
        self._events.ate.subscribe(self.ate_callback)

        self._events.died = Event()
        self.died_callback = MagicMock()
        self._events.died.subscribe(self.died_callback)