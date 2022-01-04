import win32api, win32con, win32gui, time

def press_and_release(hwnd,key):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, key, 0)
    time.sleep(.1)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, key, 0)


def click_and_release(hwnd,x,y):
    windowOffset = win32gui.GetWindowRect(hwnd)
    x, y = x - windowOffset[0], y - windowOffset[1]
    lParam = (int(y) << 16) | int(x)
    # Converts global coordinates from pyautogui to relative window
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, lParam)
    time.sleep(.1)
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)