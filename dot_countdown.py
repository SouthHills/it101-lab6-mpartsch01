from sense_emu import SenseHat
from time import sleep

sense = SenseHat()

G = [0, 255, 0]
R = [255, 0, 0]
X = [0, 0, 0]
s = 10
timer = [1]

for i in range (0, 63):#resetting the display of the color
    timer.append(X)

for i in range (0, 10):
    timer[i]= G

sense.set_pixels(timer)
for i in range (0, 10):
    timer[i]= R
    sleep(1)
    sense.set_pixels(timer)
for i in range (0,10):
    sense.clear()
    sleep(0.1)
    sense.set_pixels(timer)
    sleep(0.1)

