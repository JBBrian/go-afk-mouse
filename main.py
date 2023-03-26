import pyautogui as pag
import random
import time

count = 0

while count < 7:
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    pag.moveTo(x, y, 0.5)
    time.sleep(1)
    count += 1
    print(count)
    