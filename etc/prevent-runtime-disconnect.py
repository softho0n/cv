import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

while True :
	time.sleep(2)
	pyautogui.click(17, 391, button='left', clicks=1, interval=1)
	print("Clicked")

