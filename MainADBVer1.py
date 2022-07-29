import time
import os
from adbutils import adb
import cv2 as cv

print(os.getcwd())


def find(img_gray):
    w, h = img_gray.shape[::-1]
    # Find the width and height of the image
    res = cv.matchTemplate(screenCap_gray, img_gray, cv.TM_CCOEFF_NORMED)
    # Matching template to determine if there is any match
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return top_left, bottom_right, max_val


def initialisation():
    error_rgb = cv.imread('ADB_Assets/ErrorNotice.png')
    error_gray = cv.cvtColor(error_rgb, cv.COLOR_BGR2GRAY)
    closed_rgb = cv.imread('ADB_Assets/ClosedNotice.png')
    closed_gray = cv.cvtColor(closed_rgb, cv.COLOR_BGR2GRAY)
    miniRoom_rgb = cv.imread('ADB_Assets/MiniRoom.png')
    miniRoom_gray = cv.cvtColor(miniRoom_rgb, cv.COLOR_BGR2GRAY)
    returnError_rgb = cv.imread('ADB_Assets/ReturnErrorNotice.png')
    returnError_gray = cv.cvtColor(returnError_rgb, cv.COLOR_BGR2GRAY)
    return error_gray, closed_gray, miniRoom_gray, returnError_gray


error_gray, closed_gray, miniRoom_gray, returnError_gray = initialisation()
devices = adb.device_list()
# deviceChoice = int(input(devices))
deviceChoice = 0
d = devices[deviceChoice]
# 5574 seems to be 4gb
delay = 1.5
roomsJoined = 0
screenCapDir = str(os.getcwd()) + "\screenCap.png"

try:
    while True:
        screenFeed = d.shell(["screencap", "-p", ">", "/sdcard/screenCap.png"])
        d.sync.pull("/sdcard/screenCap.png", screenCapDir)

        screenCap_rgb = cv.imread('screenCap.png')
        screenCap_gray = cv.cvtColor(screenCap_rgb, cv.COLOR_BGR2GRAY)
        time.sleep(delay)

        miniRoomLeft, _, miniRoomConf = find(miniRoom_gray)
        if miniRoomConf > 0.95:
            roomsJoined += 1
            print(f'Join! Rooms joined since start: {roomsJoined}')
            d.click(*miniRoomLeft)
            time.sleep(delay * 2)
            # click ready
            d.click(440, 1160)
            continue

        _, _, closedConf = find(closed_gray)
        if closedConf > 0.95:
            d.click(450, 1030)
            continue

        _, _, returnErrorConf = find(returnError_gray)
        if returnErrorConf > 0.95:
            d.click(450, 1030)
            continue

        _, _, errorConf = find(error_gray)
        if errorConf > 0.95:
            for _ in range(3):
                d.click(380, 1000)
                time.sleep(4.5)
            continue
        # (285, 638), (618, 786)

except KeyboardInterrupt:
    pass

# print(find("ReadyButton.png"))
# ((376, 1132), (522, 1178))
