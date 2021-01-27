import machine
import neopixel
import time

np = neopixel.NeoPixelRing(machine.Pin(2), 60)

while True:
    t = time.localtime()
    h, m, s = (int(x) for x in t[3:6])

    # set everything else to 0
    for i in range(60):
        np[i] = (0, 0, 0)

    np[s] = (0, 0, 255)
    np[m] = (0, 255, 0)
    np[h] = (255, 0, 0)

    np.write()
    time.sleep(0.5)
