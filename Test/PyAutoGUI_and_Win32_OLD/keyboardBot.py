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

time.sleep(2)
while True:
    if currentScreen == Screens.coopScreen.value:
        keyboard.press_and_release('a')
        time.sleep(3)
        keyboard.press_and_release('d')
        time.sleep(1)
        keyboard.press_and_release('a')
        currentScreen = Screens.lobbyScreen.value
        time.sleep(2)

    elif currentScreen == Screens.lobbyScreen.value:
        for i in pyautogui.locateAllOnScreen('Assets/Matching.PNG', confidence=0.9):
            playersMissing += 1
            print(i)
        print(f"PLayers missing:{playersMissing}")

        #changeable line here
        if playersMissing <= 1:
            keyboard.press_and_release('a')
            pauseButton = pyautogui.locateCenterOnScreen(
                'Assets/PauseButton.PNG', confidence=0.7)
            if pauseButton:
                keyboard.press_and_release('f')
                currentScreen = Screens.pauseScreen.value
        else:
            print("resets")
            playersMissing = 0

    elif currentScreen == Screens.pauseScreen.value:
        time.sleep(1)
        keyboard.press_and_release('g')
        time.sleep(0.5)
        keyboard.press_and_release('d')
        currentScreen = Screens.coopScreen.value
        time.sleep(3.5)
        playersMissing = 2



