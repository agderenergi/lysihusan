import time

import pyautogui 

y_movement = 10
print("Lys i Husan v1.0 started, pressing F15 every minute.  Press Ctrl-C to end")
print("Released under the GNU General Public License v2.0 on GitHub: agderenergi/lysihusan/LICENSE")
print("For info contact hakon.klausen@ae.no")
while True:
	#pyautogui.moveRel(0, y_movement)
	#y_movement = y_movement * -1
	pyautogui.press('f15')
	time.sleep(60)
