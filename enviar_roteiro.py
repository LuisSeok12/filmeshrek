import time
import pyautogui as pg

def abrir_roteiro():
    with open("roteiroshrek.txt", "r", encoding="utf-8") as file:
        for line in file:
            pg.write(line)
            pg.press("enter")
            time.sleep(0.1)

abrir_roteiro()




