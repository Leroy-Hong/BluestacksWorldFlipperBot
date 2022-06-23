import pyautogui
import cv2 as cv
from enum import Enum
from customFunctions import *

class Screens(Enum):
    coopScreen = 0
    lobbyScreen = 1
    pauseScreen = 2

playersMissing = 0
currentScreen = 0
windowName = '4GB 4Core Portrait'
timeDelay = 3
playerRequirement = 1
#Check matching.png, PauseButton.png

hwndChild = getHwnd(windowName)
win32gui.SendMessage(hwndChild, win32con.WM_ACTIVATE, win32con.WA_CLICKACTIVE, 0)
time.sleep(2)

while True:
    if currentScreen == Screens.coopScreen.value:
        press_and_release(hwndChild,VK_CODE["a"])
        # Presses Co-Op
        time.sleep(timeDelay)
        press_and_release(hwndChild,VK_CODE["d"])
        # Presses recruit
        time.sleep(1)
        press_and_release(hwndChild,VK_CODE["a"])
        # Presses the thing after recruit
        currentScreen = Screens.lobbyScreen.value
        print("Looby screen")
        time.sleep(2)

    elif currentScreen == Screens.lobbyScreen.value:
        for i in pyautogui.locateAllOnScreen('Assets/Matching.PNG', confidence=0.9):
            playersMissing += 1
            # print(i)
        print(f"PLayers missing:{playersMissing}")
        # Counts the amount of Matching... -> missing people

        if playersMissing <= playerRequirement:
            press_and_release(hwndChild,VK_CODE["a"])
            # Press start whenever possible
            bossStart = pyautogui.locateCenterOnScreen(
                'Assets/BossStart.PNG', confidence=0.7)
            if bossStart:
                # Ensure that the pause button is pressed
                win32gui.SendMessage(hwndChild, win32con.WM_ACTIVATE, win32con.WA_CLICKACTIVE, 0)
                press_and_release(hwndChild,VK_CODE["f"])
                currentScreen = Screens.pauseScreen.value
            else:
                playersMissing = 0
        else:
            print("resets")
            playersMissing = 0

    elif currentScreen == Screens.pauseScreen.value:
        time.sleep(0.5)
        press_and_release(hwndChild,VK_CODE["g"])
        # Presses abort
        time.sleep(0.5)
        press_and_release(hwndChild,VK_CODE["d"])
        # Confirms the abort
        currentScreen = Screens.coopScreen.value
        time.sleep(timeDelay * 2)
        # Loading time from abortion to co-op screen, may vary
        playersMissing = 0



