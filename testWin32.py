import win32gui, win32api, win32con, win32ui
import time

hwnd = win32gui.FindWindow(None, '64 Main')
print(hwnd)
hwndChild = win32gui.GetWindow(hwnd, win32con.GW_CHILD)
hwndChild2 = win32gui.GetWindow(hwndChild, win32con.GW_CHILD)
"""
aa = win32ui.FindWindow(None, '64 Main')
aa.SetForegroundWindow()
aa.SetFocus()
"""
"""
win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_CLICKACTIVE, 0)
win32api.PostMessage(hwndChild, win32con.WM_KEYDOWN, 0x41, 0)
time.sleep(.1)
win32api.PostMessage(hwndChild, win32con.WM_KEYUP, 0x41, 0)
#win32gui.MoveWindow(hwndChild2, 0, 0, 0, 0, True)
"""
1581,430
x = 200
y = 500
lParam = (y << 16) | x
pt = x,y
testhwnd = win32gui.WindowFromPoint(pt)
win32api.PostMessage(hwndChild, win32con.WM_LBUTTONDOWN, 0, lParam)
time.sleep(.1)
win32api.PostMessage(hwndChild, win32con.WM_LBUTTONUP, 0, lParam)
