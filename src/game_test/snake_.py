import unittest
from unittest.mock import MagicMock
from src.game.event import Event
from src.game.event_hub import EventHub


class Snake_(unittest.IsolatedAsyncioTestCase):
    _msec = 0.001
    _small_number = 7
    _medium_number = 10
    _large_number = 20

    def __init__(self, *args, **kwargs):
        super(Snake_, self).__init__(*args, **kwargs)

    def setUp(self):
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
