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
    pause_rgb = cv.imread('ADB_Assets/PauseButton.png')
    pause_gray = cv.cvtColor(pause_rgb, cv.COLOR_BGR2GRAY)
    leave_rgb = cv.imread('ADB_Assets/LeaveButton.png')
    leave_gray = cv.cvtColor(leave_rgb, cv.COLOR_BGR2GRAY)
    next_rgb = cv.imread('ADB_Assets/NextButton.png')
    next_gray = cv.cvtColor(next_rgb, cv.COLOR_BGR2GRAY)
    closed_rgb = cv.imread('ADB_Assets/closedNotice.png')
    closed_gray = cv.cvtColor(closed_rgb, cv.COLOR_BGR2GRAY)
    error_rgb = cv.imread('ADB_Assets/ErrorNotice.png')
    error_gray = cv.cvtColor(error_rgb, cv.COLOR_BGR2GRAY)
    player_rgb = cv.imread('ADB_Assets/MatchingNotice.png')
    player_gray = cv.cvtColor(player_rgb, cv.COLOR_BGR2GRAY)
    coop_rgb = cv.imread('ADB_Assets/CoopButton.png')
    coop_gray = cv.cvtColor(coop_rgb, cv.COLOR_BGR2GRAY)
    start_rgb = cv.imread('ADB_Assets/YStartButton.png')
    start_gray = cv.cvtColor(start_rgb, cv.COLOR_BGR2GRAY)
    afk_rgb = cv.imread('ADB_Assets/AFKNotice.png')
    afk_gray = cv.cvtColor(afk_rgb, cv.COLOR_BGR2GRAY)

    return pause_gray, leave_gray, next_gray, closed_gray, error_gray, player_gray, coop_gray, start_gray, afk_gray


pause_gray, leave_gray, next_gray, closed_gray, error_gray, player_gray, coop_gray, start_gray, afk_gray = initialisation()
devices = adb.device_list()
#deviceChoice = int(input(devices))
deviceChoice = 1
d = devices[deviceChoice]
#5574 seems to be 4gb
delay = 1.5
screenCapDir = str(os.getcwd()) + "\miniScreenCap.png"

try:
    while True:
        screenFeed = d.shell(["screencap", "-p", ">", "/sdcard/miniScreenCap"])
        d.sync.pull("/sdcard/miniScreenCap", screenCapDir)

        screenCap_rgb = cv.imread("miniScreenCap.png")
        screenCap_gray = cv.cvtColor(screenCap_rgb, cv.COLOR_BGR2GRAY)
        time.sleep(delay)

        #Multibutton
        _, _, coopConf = find(coop_gray)
        if coopConf > 0.95:
            print('coop')
            d.click(400,880)
            time.sleep(delay*2)
            # Recruit
            d.click(350,825)
            time.sleep(delay*0.75)
            # Request
            d.click(525,920)
            continue

        #350, 825
        #Count players

        #Start
        _, _, startConf = find(start_gray)
        if startConf > 0.95:
            #print('start')
            d.click(300,900)
            continue

        #Find pause
        _, _, pauseConf = find(pause_gray)
        if pauseConf > 0.95:
            print('paused!')
            d.click(510, 830)
            time.sleep(0.05)
            d.click(30,30)
            time.sleep(delay*0.55)
            d.click(110,1220)
            time.sleep(delay*0.5)
            d.click(510,830)
            continue
        #Click, exit
        #110, 1220
        #514, 827
        #Restart

        _, _, afkConf = find(afk_gray)
        if afkConf > 0.95:
            d.click(365,825)

except KeyboardInterrupt:
    pass
