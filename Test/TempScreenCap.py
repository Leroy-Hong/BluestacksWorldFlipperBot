from adbutils import adb
d = adb.device()
screenFeed = d.shell(["screencap", "-p", ">", "/sdcard/screenCapTest.png"])
d.sync.pull("/sdcard/screenCapTest.png", "D:/Documents/PythonProjects/BluestacksWorldFlipper/screenCapTest.png")