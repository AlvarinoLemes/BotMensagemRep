import time
import pyautogui

for i in range (0,1000):
    pyautogui.click(519, 797)
    pyautogui.typewrite('who am I?')
    pyautogui.press('enter')
    time.sleep(0.4)