import time

from adbutils import adb
import cv2 as cv

def find(fileName):
    img_rgb = cv.imread(f'../ADB_Assets/{fileName}')
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    w, h = img_gray.shape[::-1]
    res = cv.matchTemplate(screenCap_gray, img_gray, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return top_left, bottom_right


d = adb.device()
delay = 3


try:
    while True:
        screenFeed = d.shell(["screencap", "-p", ">", "/sdcard/screenCap.png"])
        #print(screenFeed)
        d.sync.pull("/sdcard/screenCap.png", "D:/Documents/PythonProjects/BluestacksWorldFlipper/screenCap.png")

        screenCap_rgb = cv.imread('../screenCap.png')
        screenCap_gray = cv.cvtColor(screenCap_rgb, cv.COLOR_BGR2GRAY)
        time.sleep(delay)
        #print("BELL")
        bellLeft, bellRight = find("BellButton.png")
        # d.click(500, 1500) # go next
        if 30 > bellLeft[0] > 10 > bellLeft[1] and 100 > bellRight[0] > 80 > bellRight[1]:
            print("bell!")
            # (26,9) (93,76) bellbutton
            d.click(*bellLeft)
            time.sleep(0.4)
            d.click(600, 1300)
            time.sleep(3)
            d.click(380, 1140)




        #print("NEXT")
        nextLeft, nextRight = find("NextButton.png")

        if 1470 > nextLeft[1] > 1460 > 420 > nextLeft[0] > 410 and 1550 > nextRight[1] > 1530 > 490 > nextRight[
            0] > 480:
            print('next')
            # (414, 1465) (489, 1540) nextbutton
            for _ in range(2):
                d.click(*nextLeft)
                time.sleep(0.4)
        #print("LEAVE")
        leaveLeft, leaveRight = find('LeaveButton.png')

        if 1490 > leaveLeft[1] > 1480 > 170 > leaveLeft[0] > 160 and 1520 > leaveRight[1] > 1510 > 380 > leaveRight[
            0] > 370:
            print('leave')
            # (167, 1488) (371, 1516) leavebutton
            d.click(*leaveLeft)

        closedLeft, closedRight = find("closedNotice.png")
        if 640 > closedLeft[1] > 630 > 290 > closedLeft[0] > 280 and 790 > closedRight[1] > 780 > 620 > closedRight[0] > 610:
            d.click(300, 1000)

        #(285, 638), (618, 786)

except KeyboardInterrupt:
    pass
#print(find("ReadyButton.png"))
#((376, 1132), (522, 1178))



#print(leaveLeft, leaveRight)
