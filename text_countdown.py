from sense_emu import SenseHat
from time import sleep

sense_emulator = SenseHat()
G = [0, 255, 0]
R = [105, 0 , 10]
P = [150,0,150]
sense_emulator.show_letter('9', R)

for i in range( 9, 0, -1):
    R [0]+= 15
    sense_emulator.show_letter(f'{i}', R)
    sleep(1)
sense_emulator.show_letter(f'0', P)
