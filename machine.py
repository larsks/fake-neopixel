'''This is a dummy replacement for the Micropython machine module.

It exists so that calls to `machine.Pin(n)` run without error.'''


class Pin:
    def __init__(self, pin):
        self.pin = pin
