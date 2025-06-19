import pyautogui
import time

# Espera 3 segundos para que te dé tiempo de enfocar la ventana del juego
time.sleep(1)

# click en una img
btn = pyautogui.locateOnScreen('init1.png', confidence=0.8)
if btn:
    pyautogui.click(pyautogui.center(btn))
    time.sleep(1)
btn = pyautogui.locateOnScreen('init3.png', confidence=0.8)
if btn:
    pyautogui.click(pyautogui.center(btn))
    time.sleep(30)
    pyautogui.moveTo(700, 700)
    pyautogui.click()
time.sleep(30)
btn = pyautogui.locateOnScreen('forjaMaterialesInit.png', confidence=0.8)
if btn:
    pyautogui.click(pyautogui.center(btn))
    time.sleep(1)
