import win32gui, win32api, win32con
import pyautogui
import cv2 as cv
import time

windowName = '64 main'
hwnd = win32gui.FindWindow(None, windowName)
if hwnd:
    hwndChild = win32gui.GetWindow(hwnd, win32con.GW_CHILD)
    if hwndChild:
        pass
    else:
        print("hwnd child not found")
        exit()
else:
    print("hwnd not found")
    exit()


def click_and_release(x,y):
    windowOffset = win32gui.GetWindowRect(hwndChild)
    print(windowOffset)
    x, y = x - windowOffset[0], y - windowOffset[1]
    lParam = (int(y) << 16) | int(x)
    pt = x, y
    print(f"clicked{pt}")
    # clickedhwnd = win32gui.WindowFromPoint(pt)
    win32api.PostMessage(hwndChild, win32con.WM_LBUTTONDOWN, 0, lParam)
    time.sleep(.1)
    win32api.PostMessage(hwndChild, win32con.WM_LBUTTONUP, 0, lParam)

refreshButton = pyautogui.locateCenterOnScreen(
                '../Assets/RefreshListButton.PNG', confidence=0.8)
click_and_release(refreshButton.x,refreshButton.y)
#print(refreshButton.x,refreshButton.y)
time.sleep(5)
refreshButton = pyautogui.locateCenterOnScreen(
                '../Assets/RefreshListButton.PNG', confidence=0.8)
click_and_release(refreshButton.x,refreshButton.y)