import machine
import neopixel
import time

led_count = 30

np = neopixel.NeoPixelRing(machine.Pin(2), led_count)

while True:
    for i in range(led_count):

        for j in range(6):
            cj = led_count*j
            np[(i-j) % led_count] = (0, 255-cj, 255-cj)

        for j in range(6):
            cj = led_count*j
            np[(60-i+15-j) % led_count] = (255-cj, 0, 255-cj)

        np.write()
        time.sleep(0.05)
