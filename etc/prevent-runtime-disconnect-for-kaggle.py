import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
clink_cnt = 0

while True :
	time.sleep(5)
	pyautogui.click(1390, 171, button='left', clicks=1, interval=1)
	print(f'Clicked {clink_cnt}')
	clink_cnt += 1

