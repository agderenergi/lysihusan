import time

import pyautogui 

y_movement = 10
print("Lys i Husan started, pressing F15 every second...  Press Ctrl-C to end")
while True:
	#pyautogui.moveRel(0, y_movement)
	#y_movement = y_movement * -1
	pyautogui.press('f15')
	time.sleep(1)
