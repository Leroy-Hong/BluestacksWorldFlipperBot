import keyboard
import pyautogui
import cv2 as cv
import time
from enum import Enum

class Screens(Enum):
    coopScreen = 0
    winScreen = 1
    pauseScreen = 2

isPaused = False
playersMissing = 0
currentScreen = 0

time.sleep(2)
while True:
    if currentScreen == Screens.coopScreen.value:
        miniRoom = pyautogui.locateCenterOnScreen('Assets/MiniRoom.PNG', confidence=0.92)
        if miniRoom:
            print(miniRoom)
            pyautogui.click(x=miniRoom.x, y=miniRoom.y, clicks=1, button='left')
            time.sleep(3.5)
            print("AAA")
        else:
            refreshButton = pyautogui.locateCenterOnScreen(
                'Assets/RefreshListButton.PNG', confidence=0.95)
            if refreshButton:
                pyautogui.click(x=refreshButton.x, y=refreshButton.y, clicks=1, button='left')
        readyMainButton = pyautogui.locateCenterOnScreen(
                'Assets/ReadyMainButton.PNG', confidence=0.95)
        if readyMainButton:
            pyautogui.click(x=readyMainButton.x, y=readyMainButton.y, clicks=1, button='left')
            time.sleep(1)
            currentScreen = Screens.winScreen.value
            time.sleep(2)

    elif currentScreen == Screens.winScreen.value:
        questResult = pyautogui.locateOnScreen(
            'Assets/QuestResult.PNG', confidence=0.9)
        if questResult:
            smallNext = pyautogui.locateCenterOnScreen(
            'Assets/SmallNext.PNG', confidence=0.9)
            smallLeave = pyautogui.locateCenterOnScreen(
            'Assets/SmallLeave.PNG', confidence=0.9)
            if smallNext:
                pyautogui.click(x=smallNext.x, y=smallNext.y, clicks=4, interval=0.1, button='left')
            elif smallLeave:
                time.sleep(1)
                pyautogui.click(x=smallLeave.x, y=smallLeave.y, clicks=1, button='left')
                currentScreen = Screens.coopScreen.value
                time.sleep(7)

    #elif currentScreen == Screens.pauseScreen.value:




