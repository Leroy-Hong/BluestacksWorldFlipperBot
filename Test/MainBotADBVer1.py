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
import os
#print(adb.device_list())


# You do not need to offer serial if only one device connected
# RuntimeError will be raised if multi device connected
#print(os.listdir())
d = adb.device()
#serial = d.shell(["getprop", "ro.serial"]) # 获取Prop信息

screenFeed = d.shell(["screencap", "-p", ">", "/sdcard/screenCap.png"])
print(screenFeed)
d.sync.pull("/sdcard/screenCap.png", "D:/Documents/PythonProjects/BluestacksWorldFlipper/screenCap.png")

screenCap_rgb = cv.imread('../screenCap.png')
screenCap_gray = cv.cvtColor(screenCap_rgb, cv.COLOR_BGR2GRAY)


bell_rgb = cv.imread('../ADB_Assets/BellButton.png')
bell_gray = cv.cvtColor(bell_rgb, cv.COLOR_BGR2GRAY)
w, h = bell_gray.shape[::-1]

res = cv.matchTemplate(screenCap_gray,bell_gray,cv.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
print("BELL")
print(top_left,bottom_right)
# d.click(500, 1500) # go next
if 30 > top_left[0] > 10 > top_left[1] and 100 > bottom_right[0] > 80 > bottom_right[1]:
    print("bell!")
    d.click(*top_left)
    time.sleep(0.4)
    d.click(600,1000)

next_rgb = cv.imread('../ADB_Assets/NextButton.png')
next_gray = cv.cvtColor(next_rgb, cv.COLOR_BGR2GRAY)
w, h = next_gray.shape[::-1]
#(414, 1465) (489, 1540)
#(291, 1465) (366, 1540)
res = cv.matchTemplate(screenCap_gray,next_gray,cv.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
print("NEXT")
print(top_left,bottom_right)
# show property, also based on d.shell
if 410 < top_left[0] < 420 and 1470 > top_left[1] > 1460:
    print('adf')
    d.click(414, 1465)

leave_rgb = cv.imread('../ADB_Assets/LeaveButton.png')
leave_gray = cv.cvtColor(next_rgb, cv.COLOR_BGR2GRAY)
w, h = leave_gray.shape[::-1]

res = cv.matchTemplate(screenCap_gray,leave_gray,cv.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
print("LEAVE")
print(top_left,bottom_right)
print('teste')
print(find('BellButton.png'))
'''
print(d.prop.name) # output example: surabaya
d.prop.model
d.prop.device


d.prop.get("ro.product.model")
d.prop.get("ro.product.model", cache=True) # a little faster, use cache data first

d.get_serialno() # same as adb get-serialno
d.get_devpath() # same as adb get-devpath
d.get_state() # same as adb get-state'''