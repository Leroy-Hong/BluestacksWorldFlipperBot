from customFunctions import *
import pyautogui

class Button:
    def __init__(self, left, top, width, height, scale):
        self.dimension = (left*scale,top*scale,
                          width*scale,height*scale)

def getScale(windowName, defaultBreadth):
    hwnd = getHwnd(windowName)
    hwndWindowDimensions = win32gui.GetWindowRect(hwnd)
    hwndWindowBreadth = hwndWindowDimensions[2]- hwndWindowDimensions[0]
    return hwndWindowBreadth / defaultBreadth

def calibrateButton(prompt, scale, left, top, width, height, name):
    input(prompt)
    calibratedButton = Button(left, top, width, height, scale)
    print(calibratedButton.dimension)
    im = pyautogui.screenshot(region=calibratedButton.dimension)
    im.save(f"Assets/{name}.PNG")
    print(f"Saved {name}")

#Callibration start
miniScale = getScale("4GB 4Core Portrait", 319)
print(miniScale)
mainScale = getScale("64 Main", 439)
print(mainScale)

calibrateButton("Quest result screen is visible",
                mainScale,
                397,64,287,45,
                "QuestResult")

calibrateButton("Ensure refresh list is unclicked and visible",
                mainScale,
                708,204,30,34,
                "RefreshListButton")

calibrateButton("Req backup first before continuing",
                miniScale,
                218,159,72,39,
                "Matching")

calibrateButton("Refresh list until mini room is visible",
                mainScale,
                442,354,148,27,
                "MiniRoom")

calibrateButton("Ensure pause button is visible",
                miniScale,
                10,53,20,28,
                "PauseButton")

calibrateButton("Quest result screen is visible",
                mainScale,
                397,64,287,45,
                "QuestResult")

input("Process should be completed!")