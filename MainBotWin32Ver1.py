import win32gui, win32api, win32con
import pyautogui
import cv2 as cv
import time
from enum import Enum
from customFunctions import *

class Screens(Enum):
    coopScreen = 0
    winScreen = 1

currentScreen = 0
questResultSeen = False
windowName = '64 main'
timeDelay = 4

hwndChild = getHwnd(windowName)

#miniroom.png, refreshlistbutton.png, questResult.png
win32gui.SendMessage(hwndChild, win32con.WM_ACTIVATE, win32con.WA_CLICKACTIVE, 0)
time.sleep(2)

while True:
    if currentScreen == Screens.coopScreen.value:
        #\\
        miniRoom = pyautogui.locateCenterOnScreen('Assets/MiniRoom.PNG', confidence=0.8)
        if miniRoom:
            print(miniRoom)
            click_and_release(hwndChild, miniRoom.x, miniRoom.y)
            # Joins the room, delay for loading may vary (default = 4)
            time.sleep(timeDelay)
            press_and_release(hwndChild, VK_CODE['a'])
            # Presses ready, idk what the delay is for
            time.sleep(3)
            currentScreen = Screens.winScreen.value
        else:
            refreshButton = pyautogui.locateCenterOnScreen(
                'Assets/RefreshListButton.PNG', confidence=0.95)
            if refreshButton:
                click_and_release(hwndChild, refreshButton.x, refreshButton.y)
                # Presses refresh list
                time.sleep(1)
        #\\
    elif currentScreen == Screens.winScreen.value:
        #\\
        questResult = pyautogui.locateOnScreen(
            'Assets/QuestResult.PNG', confidence=0.7)
        if questResult:
            win32gui.SendMessage(hwndChild, win32con.WM_ACTIVATE, win32con.WA_CLICKACTIVE, 0)
            press_and_release(hwndChild, VK_CODE['s'])
            # Presses next and or leave room
            questResultSeen = True
        elif not questResult and questResultSeen:
            # if there is no quest result but it has been seen
            questResultSeen = False
            currentScreen = Screens.coopScreen.value
        #\\


