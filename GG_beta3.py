import pyautogui as pg
import time
import keyboard 
import os


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
   

pg.hotkey('win', 'd')
save_directory = "C:\\Users\\Public\\Public Pictures"  
file_name = "screenshot"
t_sh(save_directory, file_name)
image  = "C:\\Users\\Public\\Public Pictures\\screenshot.png"
while bool:
    if keyboard.is_pressed(key3) and keyboard.is_pressed(key) and keyboard.is_pressed(key2) and keyboard.is_pressed(key4):
        os.remove(image)
        bool = False
    else:
        try:
             
            x, y = pg.locateCenterOnScreen(image, confidence=0.8)   
           
            time.sleep(1)

        except Exception as e: 
            pg.hotkey('alt','f4')
            time.sleep(0.5)
