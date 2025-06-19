import pyautogui
import time

# Espera 3 segundos para que te dé tiempo de enfocar la ventana del juego
time.sleep(1)

# click en una img
btn = pyautogui.locateOnScreen('recolectar.png', confidence=0.8)
if btn:
    pyautogui.click(pyautogui.center(btn))