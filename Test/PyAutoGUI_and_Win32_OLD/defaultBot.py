import keyboard
import pyautogui
import cv2 as cv
import time

isRecruited = False
isPaused = False
playersMissing = 0
while True:
    coopButton = pyautogui.locateCenterOnScreen('Assets/CoopButton.PNG', confidence=0.9)
    recruitButton = pyautogui.locateCenterOnScreen('Assets/RecruitButton.PNG', confidence=0.9)
    reqBackupButton = pyautogui.locateCenterOnScreen('Assets/ReqBackupButton.PNG', confidence=0.7)

    if coopButton:
        print(coopButton)
        pyautogui.click(x=coopButton.x, y=coopButton.y, clicks=1, button='left')
    if not isRecruited:
        #performs a recruit
        if recruitButton:
            print(recruitButton)
            pyautogui.click(x=recruitButton.x, y=recruitButton.y, clicks=1, button='left')

        if reqBackupButton:
            print(reqBackupButton)
            pyautogui.click(x=reqBackupButton.x, y=reqBackupButton.y, clicks=1, button='left')
            isRecruited = True
    else:
        #locates amount of players
        for i in pyautogui.locateAllOnScreen('Assets/Matching.PNG', confidence=0.9):
            playersMissing += 1
            print(i)
        print(f"PLayers missing:{playersMissing}")

        #changeable line here
        if playersMissing <= 1:
            startButton = pyautogui.locateCenterOnScreen(
                'Assets/StartButton.PNG', confidence=0.9)
            pauseButton = pyautogui.locateCenterOnScreen(
                'Assets/PauseButton.PNG', confidence=0.7)
            abortButton = pyautogui.locateCenterOnScreen(
                'Assets/AbortButton.PNG', confidence=0.7)

            if startButton:
                pyautogui.click(x=startButton.x, y=startButton.y, clicks=1, button='left')
            elif isPaused:
                #in pause menu
                if abortButton:
                    pyautogui.click(x=abortButton.x, y=abortButton.y, clicks=1, button='left')
                time.sleep(1)
                yesButton = pyautogui.locateCenterOnScreen(
                    'Assets/YesButton.PNG', confidence=0.7)
                if yesButton:
                    pyautogui.click(x=yesButton.x, y=yesButton.y, clicks=1, button='left')
                    isPaused = False
                    isRecruited = False
                    playersMissing = 0
            elif pauseButton:
                #presses pausebutton in game
                pyautogui.click(x=pauseButton.x, y=pauseButton.y, clicks=1, button='left')
                isPaused = True
        else:
            print("resets")
            playersMissing = 0


