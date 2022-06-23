import time

from adbutils import adb
import cv2 as cv


def find(img_gray):
    w, h = img_gray.shape[::-1]
    res = cv.matchTemplate(screenCap_gray, img_gray, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return top_left, bottom_right


def initialisation():
    bell_rgb = cv.imread(f'../ADB_Assets/BellButton.png')
    bell_gray = cv.cvtColor(bell_rgb, cv.COLOR_BGR2GRAY)
    leave_rgb = cv.imread(f'../ADB_Assets/LeaveButton.png')
    leave_gray = cv.cvtColor(leave_rgb, cv.COLOR_BGR2GRAY)
    next_rgb = cv.imread(f'../ADB_Assets/NextButton.png')
    next_gray = cv.cvtColor(next_rgb, cv.COLOR_BGR2GRAY)

    return bell_gray, leave_gray, next_gray

def roomIdentifier():
    bellLeft, bellRight = find(bell_gray)
    # d.click(500, 1500) # go next
    if 30 > bellLeft[0] > 10 > bellLeft[1] and 100 > bellRight[0] > 80 > bellRight[1]:
        print("bell!")
        # (26,9) (93,76) bellbutton
        d.click(*bellLeft)
        time.sleep(0.4)
        d.click(600, 1300)
        time.sleep(3)
        d.click(380, 1140)
        return 1
    else:
        nextLeft, nextRight = find(next_gray)

        if 1470 > nextLeft[1] > 1460 > 420 > nextLeft[0] > 410 and 1550 > nextRight[1] > 1530 > 490 > nextRight[
            0] > 480:
            print('next')
            # (414, 1465) (489, 1540) nextbutton
            for _ in range(2):
                d.click(*nextLeft)
                time.sleep(0.2)
            return 0
        else:
            leaveLeft, leaveRight = find(leave_gray)

            if 1490 > leaveLeft[1] > 1480 > 170 > leaveLeft[0] > 160 and 1520 > leaveRight[1] > 1510 > 380 > leaveRight[
                0] > 370:
                print('leave')
                # (167, 1488) (371, 1516) leavebutton
                d.click(*leaveLeft)
                return 0
            else:
                print('room not found')
                quit()

bell_gray, leave_gray, next_gray = initialisation()
d = adb.device()


screenFeed = d.shell(["screencap", "-p", ">", "/sdcard/screenCap.png"])
d.sync.pull("/sdcard/screenCap.png", "D:/Documents/PythonProjects/BluestacksWorldFlipper/screenCap.png")
screenCap_rgb = cv.imread('../screenCap.png')
screenCap_gray = cv.cvtColor(screenCap_rgb, cv.COLOR_BGR2GRAY)

currentRoom = roomIdentifier()

try:
    while True:
        screenFeed = d.shell(["screencap", "-p", ">", "/sdcard/screenCap.png"])
        d.sync.pull("/sdcard/screenCap.png", "D:/Documents/PythonProjects/BluestacksWorldFlipper/screenCap.png")

        screenCap_rgb = cv.imread('../screenCap.png')
        screenCap_gray = cv.cvtColor(screenCap_rgb, cv.COLOR_BGR2GRAY)
        time.sleep(5)

        if currentRoom == 0:
            bellLeft, bellRight = find(bell_gray)
            # d.click(500, 1500) # go next
            if 30 > bellLeft[0] > 10 > bellLeft[1] and 100 > bellRight[0] > 80 > bellRight[1]:
                print("bell!")
                # (26,9) (93,76) bellbutton
                d.click(*bellLeft)
                time.sleep(0.4)
                d.click(600, 1300)
                time.sleep(3)
                d.click(380, 1140)
                currentRoom = 1
        elif currentRoom == 1:
            nextLeft, nextRight = find(next_gray)

            if 1470 > nextLeft[1] > 1460 > 420 > nextLeft[0] > 410 and 1550 > nextRight[1] > 1530 > 490 > nextRight[
                0] > 480:
                print('next')
                # (414, 1465) (489, 1540) nextbutton
                for _ in range(2):
                    d.click(*nextLeft)
                    time.sleep(0.2)
                currentRoom = 0
            else:
                leaveLeft, leaveRight = find(leave_gray)
                if 1490 > leaveLeft[1] > 1480 > 170 > leaveLeft[0] > 160 and 1520 > leaveRight[1] > 1510 > 380 > leaveRight[
                    0] > 370:
                    print('leave')
                    # (167, 1488) (371, 1516) leavebutton
                    d.click(*leaveLeft)
                    currentRoom = 0

except KeyboardInterrupt:
    pass
# print(find("ReadyButton.png"))
# ((376, 1132), (522, 1178))


# print(leaveLeft, leaveRight)
