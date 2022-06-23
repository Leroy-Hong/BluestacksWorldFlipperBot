import time
import os
from adbutils import adb
import cv2 as cv

print(os.getcwd())
def find(img_gray):
    w, h = img_gray.shape[::-1]
    res = cv.matchTemplate(screenCap_gray, img_gray, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return top_left, bottom_right, max_val


def initialisation():
    bell_rgb = cv.imread('../ADB_Assets/BellButton.png')
    bell_gray = cv.cvtColor(bell_rgb, cv.COLOR_BGR2GRAY)
    leave_rgb = cv.imread('../ADB_Assets/LeaveButton.png')
    leave_gray = cv.cvtColor(leave_rgb, cv.COLOR_BGR2GRAY)
    next_rgb = cv.imread('../ADB_Assets/NextButton.png')
    next_gray = cv.cvtColor(next_rgb, cv.COLOR_BGR2GRAY)
    closed_rgb = cv.imread('../ADB_Assets/closedNotice.png')
    closed_gray = cv.cvtColor(closed_rgb, cv.COLOR_BGR2GRAY)
    error_rgb = cv.imread('../ADB_Assets/ErrorNotice.png')
    error_gray = cv.cvtColor(error_rgb, cv.COLOR_BGR2GRAY)

    return bell_gray, leave_gray, next_gray, closed_gray, error_gray


bell_gray, leave_gray, next_gray, closed_gray, error_gray = initialisation()
d = adb.device()
delay = 2

try:
    while True:
        screenFeed = d.shell(["screencap", "-p", ">", "/sdcard/screenCap.png"])
        d.sync.pull("/sdcard/screenCap.png", "D:/Documents/PythonProjects/BluestacksWorldFlipper/screenCap.png")

        screenCap_rgb = cv.imread('../screenCap.png')
        screenCap_gray = cv.cvtColor(screenCap_rgb, cv.COLOR_BGR2GRAY)
        time.sleep(delay)

        bellLeft, bellRight, bellConf = find(bell_gray)
        # d.click(500, 1500) # go next
        if bellConf > 0.90:
            print("bell!")
            # (26,9) (93,76) bellbutton
            d.click(*bellLeft)
            time.sleep(0.4)
            d.click(600, 1300)
            time.sleep(3)
            d.click(380, 1140)

        nextLeft, nextRight, nextConf = find(next_gray)

        if nextConf > 0.95:
            print('next')
            # (414, 1465) (489, 1540) nextbutton
            for _ in range(3):
                d.click(450,1465)
                time.sleep(0.2)

        leaveLeft, leaveRight, leaveConf = find(leave_gray)

        if leaveConf > 0.95:
            print('leave')
            # (167, 1488) (371, 1516) leavebutton
            d.click(*leaveLeft)

        closedLeft, closedRight, closedConf = find(closed_gray)
        if closedConf > 0.95:
            print('closed')
            d.click(300, 1000)

        errorLeft, errorRight, errorConf = find(error_gray)
        if errorConf > 0.95:
            for _ in range(3):
                d.click(380, 1000)
                time.sleep(4.5)

        # (285, 638), (618, 786)

except KeyboardInterrupt:
    pass
# print(find("ReadyButton.png"))
# ((376, 1132), (522, 1178))
