'''tkinter-based simulation of Micropython neopixel module.

See https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html
for API documentation.
'''

import math
import threading
import time
import tkinter as tk


class NeoPixel(threading.Thread):
    LED_RADIUS = 6      # How big are LEDs?
    LED_PADDING = 5     # How much spacing in between?

    def __init__(self, pin, led_count):
        super().__init__(daemon=True)

        self.led_count = led_count
        self.leds = []
        self.led_state = [(0, 0, 0)] * led_count
        self.started = False
        self.start()

        while not self.started:
            time.sleep(0.1)

    def run(self):
        self.root = tk.Tk()
        self.create_canvas()
        self.leds = [self.draw_led(x) for x in range(self.led_count)]
        self.canvas.pack()

        self.started = True

        tk.mainloop()

    def create_canvas(self):
        self.canvas = tk.Canvas(
            self.root,
            bg='white',
            height=(self.LED_RADIUS * 2) + (self.LED_PADDING * 2),
            width=((self.LED_RADIUS * 2) + self.LED_PADDING) * self.led_count)

    def draw_led(self, pos):
        r = self.LED_RADIUS
        x = ((r * 2) + self.LED_PADDING) * pos
        y = r/2

        return self.canvas.create_oval(x, y, x+2*r, y+2*r, fill='white')

    def __setitem__(self, index, v):
        if not isinstance(v, tuple) or len(v) != 3:
            raise ValueError(v)

        self.led_state[index] = v

    def update_leds(self):
        for i, state in enumerate(self.led_state):
            color = '#{:02x}{:02x}{:02x}'.format(*state)
            self.canvas.itemconfig(self.leds[i], fill=color)

    def write(self, *args):
        self.update_leds()


class NeoPixelRing(NeoPixel):
    LED_RADIUS = 10

    def create_canvas(self):
        self.circ = self.LED_RADIUS * self.led_count

        height, _ = self.point_from_angle(90)
        width = height = height + self.LED_RADIUS*2

        self.canvas = tk.Canvas(
            self.root,
            bg='white',
            width=width,
            height=height,
        )

    def draw_led(self, pos):
        angle = (360.0 / self.led_count) * pos

        x, y = self.point_from_angle(angle)

        r = self.LED_RADIUS
        return self.canvas.create_oval(x-r, y-r, x+r, y+r, fill='black')

    def create_circle(self, r, x, y):
        return self.canvas.create_oval(x-r, y-r, x+r, y+r, fill='black')

    def point_from_angle(self, angle):
        angle_r = math.radians((angle-90) % 360)

        r_led = self.LED_RADIUS
        r_ring = self.circ//2
        x = int(r_ring * math.cos(angle_r)) + r_ring + r_led
        y = int(r_ring * math.sin(angle_r)) + r_ring + r_led

        return (x, y)


if __name__ == '__main__':
    np = NeoPixelRing(None, 60)
