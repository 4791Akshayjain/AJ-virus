import pyautogui as pg
import time
import keyboard
import os
import sys

pg.FAILSAFE = False

bool = True
key = "a"
key2 = "j"
key3 = "ctrl"
key4 = "v"

def t_sh(save_path, file_name):
    time.sleep(2)
    os.makedirs(save_path, exist_ok=True)
    screenshot = pg.screenshot()
    file_path = os.path.join(save_path, f"{file_name}.png")
    screenshot.save(file_path)
    return file_path

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

image2 = os.path.join(base_path, "kill_switch.png")

pg.hotkey('win', 'd')

save_directory = "C:\\Users\\Public\\Public Pictures"
file_name = "screenshot"

image = t_sh(save_directory, file_name)

while bool:
    if keyboard.is_pressed(key3) and keyboard.is_pressed(key) and keyboard.is_pressed(key2) and keyboard.is_pressed(key4):
        os.remove(image)
        bool = False
    else:
        try:
            location2 = pg.locateCenterOnScreen(image2, confidence=0.7, grayscale=True)
            if location2:
                pg.press('enter')

        except pg.ImageNotFoundException:
            pass

        try:
            location = pg.locateCenterOnScreen(image, confidence=0.7, grayscale=True)
            if location:
                x, y = location
                time.sleep(1)
            else:
                pg.hotkey('alt', 'f4')
                time.sleep(0.5)
        except pg.ImageNotFoundException:
            pg.hotkey('alt', 'f4')
            time.sleep(0.5)

        time.sleep(0.1)