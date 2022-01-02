import keyboard
import pyautogui
import cv2 as cv
import time

playersMissing = 0
while True:
    nextButton = pyautogui.locateCenterOnScreen('D:\Documents\PythonProjects\BluestacksWorldFlipper/NextButton.PNG',
                                                confidence=0.7)
    if nextButton:
        pyautogui.click(x=nextButton.x, y=nextButton.y, clicks=1, button='left')
    # locates amount of players
    for i in pyautogui.locateAllOnScreen('D:\Documents\PythonProjects\BluestacksWorldFlipper\Matching.PNG',
                                         confidence=0.9):
        playersMissing += 1
        print(i)
    print(f"PLayers missing:{playersMissing}")

    # changeable line here
    if playersMissing <= 1:
        startButton = pyautogui.locateCenterOnScreen(
            'D:\Documents\PythonProjects\BluestacksWorldFlipper\StartButton.PNG', confidence=0.7)
        returnButton = pyautogui.locateCenterOnScreen(
            'D:\Documents\PythonProjects\BluestacksWorldFlipper\ReturnToRoomButton.PNG', confidence=0.7)
        if startButton:
            pyautogui.click(x=startButton.x, y=startButton.y, clicks=1, button='left')
        if returnButton:
            pyautogui.click(x=returnButton.x, y=returnButton.y, clicks=1, button='left')
            playersMissing = 2
    else:
        print("resets")
        playersMissing = 0
