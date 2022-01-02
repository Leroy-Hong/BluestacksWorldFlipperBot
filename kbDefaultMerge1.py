import keyboard
import pyautogui
import cv2 as cv
import time
from enum import Enum

class Screens(Enum):
    coopScreen = 0
    lobbyScreen = 1
    pauseScreen = 2

isPaused = False
playersMissing = 0
currentScreen = 0

requiredPlayers = 1
recruitDelay = 3

time.sleep(2)
while True:
    if currentScreen == Screens.coopScreen.value:
        coopButton = pyautogui.locateCenterOnScreen('D:\Documents\PythonProjects\BluestacksWorldFlipper\CoopButton.PNG', confidence=0.9)
        if coopButton:
            print(coopButton)
            pyautogui.click(x=coopButton.x, y=coopButton.y, clicks=1, button='left')
            time.sleep(recruitDelay)
            print("RECUIRT")
            recruitButton = pyautogui.locateCenterOnScreen(
                'D:\Documents\PythonProjects\BluestacksWorldFlipper\RecruitButton.PNG', confidence=0.9)
            if recruitButton:
                pyautogui.click(x=recruitButton.x, y=recruitButton.y, clicks=1, button='left')
            time.sleep(1)
            reqBackupButton = pyautogui.locateCenterOnScreen(
                'D:\Documents\PythonProjects\BluestacksWorldFlipper\ReqBackupButton.PNG', confidence=0.7)
            if reqBackupButton:
                pyautogui.click(x=reqBackupButton.x, y=reqBackupButton.y, clicks=1, button='left')

                currentScreen = Screens.lobbyScreen.value
                time.sleep(2)

    elif currentScreen == Screens.lobbyScreen.value:
        for i in pyautogui.locateAllOnScreen('D:\Documents\PythonProjects\BluestacksWorldFlipper\Matching.PNG', confidence=0.9):
            playersMissing += 1
            print(i)
        print(f"PLayers missing:{playersMissing}")

        #changeable line here
        if playersMissing <= requiredPlayers:
            startButton = pyautogui.locateCenterOnScreen(
                'D:\Documents\PythonProjects\BluestacksWorldFlipper\StartButton.PNG', confidence=0.9)
            if startButton:
                pyautogui.click(x=startButton.x, y=startButton.y, clicks=1, button='left')
            else:
                playersMissing = 0

            pauseButton = pyautogui.locateCenterOnScreen(
                'D:\Documents\PythonProjects\BluestacksWorldFlipper\PauseButton.PNG', confidence=0.7)
            if pauseButton:
                pyautogui.click(x=pauseButton.x, y=pauseButton.y, clicks=1, button='left')
                time.sleep(0.5)
                abortButton = pyautogui.locateCenterOnScreen(
                    'D:\Documents\PythonProjects\BluestacksWorldFlipper\AbortButton.PNG', confidence=0.7)
                if abortButton:
                    currentScreen = Screens.pauseScreen.value
        else:
            print("resets")
            playersMissing = 0

    elif currentScreen == Screens.pauseScreen.value:
        print("Im pausescreen")
        abortButton = pyautogui.locateCenterOnScreen(
            'D:\Documents\PythonProjects\BluestacksWorldFlipper\AbortButton.PNG', confidence=0.7)
        yesButton = pyautogui.locateCenterOnScreen(
            'D:\Documents\PythonProjects\BluestacksWorldFlipper\YesButton.PNG', confidence=0.7)
        if yesButton:
            pyautogui.click(x=yesButton.x, y=yesButton.y, clicks=1, button='left')
            currentScreen = Screens.coopScreen.value
            time.sleep(3.5)
            playersMissing = 0
        elif abortButton:
            pyautogui.click(x=abortButton.x, y=abortButton.y, clicks=1, button='left')
            time.sleep(1)




