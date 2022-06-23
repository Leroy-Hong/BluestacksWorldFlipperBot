import pyautogui
from customFunctions import *

bossBattleButton = pyautogui.locateAllOnScreen('../Assets/QuestResult.PNG', confidence=0.7)
#if bossBattleButton:
#   pyautogui.click(x=bossBattleButton.x, y=bossBattleButton.y, clicks=1, button='left')
for i in bossBattleButton:
    print(i)
'''
hwnd = getHwnd('64 Main')
print(win32gui.GetWindowRect(hwnd))

print(762 -323)
hwnd = getHwnd('4GB 4Core Portrait')
print(win32gui.GetWindowRect(hwnd))'''