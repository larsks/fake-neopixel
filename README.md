# NeoPixel simulator for Python

This provides a `NeoPixel` and `NeoPixelRing` classes that are
API-compatible with the [MicroPython][] [`neopixel` module][neopixel].

The `NeoPixel` class creates a horizontal array of LEDs, while the
`NeoPixelRing` class creates a ring.

![Example of NeoPixelRing](images/cycle.gif)

## Examples

- `PYTHONPATH=$PWD python examples/clock.py`
- `PYTHONPATH=$PWD python examples/cycle1.py`
- `PYTHONPATH=$PWD python examples/cycle2.py`

## Requirements

This requires the `tkinter` module.

[micropython]: https://micropython.org
[neopixel]: https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html
