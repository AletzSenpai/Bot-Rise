import pyautogui
import time

# Espera 3 segundos para que te dé tiempo de enfocar la ventana del juego
time.sleep(3)

# click en una img
btn = pyautogui.locateOnScreen('recolectar.png', confidence=0.8)
if btn:
    pyautogui.click(pyautogui.center(btn))

# Mueve el mouse a la posición (500, 500) y hace clic
pyautogui.moveTo(500, 500)
#pyautogui.click()

# Escribe un texto (como en un chat del juego)
#pyautogui.write('electryxs')
#pyautogui.press('enter')
