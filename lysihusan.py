import time

import pyautogui 

pyautogui.FAILSAFE = True
print("Lys i Husan v1.1 started, Pressing F15 every minute.  Close window to end")
print("Released under the GNU General Public License v2.0 on GitHub: agderenergi/lysihusan/LICENSE")
print("For info contact hakon.klausen@ae.no")
while True:
	try:
		pyautogui.press('f15')
		time.sleep(59)
	except:
		continue
