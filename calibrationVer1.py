from customFunctions import *
import pyautogui

class Button:
    def __init__(self, xOffset1, xOffset2, yOffset1, yOffset2, scale):
        self.dimension = (xOffset1*scale,yOffset1*scale,
                          xOffset2*scale,yOffset2*scale)

def getScale(windowName, defaultBreadth):
    hwnd = getHwnd(windowName)
    hwndWindowDimensions = win32gui.GetWindowRect(hwnd)
    hwndWindowBreadth = hwndWindowDimensions[2]- hwndWindowDimensions[0]
    return hwndWindowBreadth / defaultBreadth

def calibrateButton(prompt,scale,x1,x2,y1,y2,name):
    input(prompt)
    calibratedButton = Button(x1, x2, y1, y2, scale)
    im = pyautogui.screenshot(region=calibratedButton.dimension)
    im.save(f"../Assets/{name}.PNG")
    print(f"Saved {name}")

#Callibration start
miniScale = getScale("4GB 4Core Portrait", 9999)
mainScale = getScale("64 Main", 9999)

calibrateButton("Ensure refresh list is unclicked and visible",
                mainScale,
                0,0,0,0,
                "RefreshListButton")

calibrateButton("Req backup first before continuing",
                miniScale,
                0,0,0,0,
                "Matching")

calibrateButton("Refresh list until mini room is visible",
                mainScale,
                0,0,0,0,
                "MiniRoom")

calibrateButton("Ensure pause button is visible",
                miniScale,
                0,0,0,0,
                "PauseButton")

calibrateButton("Quest result screen is visible",
                mainScale,
                0,0,0,0,
                "QuestResult")

input("Process should be completed!")