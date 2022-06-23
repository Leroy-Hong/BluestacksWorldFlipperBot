import keyboard
import pyautogui
import cv2 as cv

bossBattleButton = pyautogui.locateCenterOnScreen('Assets/BossBattlesButton.PNG', confidence=0.9)
if bossBattleButton:
    pyautogui.click(x=bossBattleButton.x, y=bossBattleButton.y, clicks=1, button='left')

golemButton = pyautogui.locateCenterOnScreen('Assets/GolemButton.PNG', confidence=1)
if golemButton:
    pyautogui.click(x=golemButton.x, y=golemButton.y, clicks=1, button='left')

golemAdvDiff = pyautogui.locateCenterOnScreen('Assets/GolemAdvancedDiff.PNG', confidence=1)
if golemAdvDiff:
    pyautogui.click(x=golemAdvDiff.x, y=golemAdvDiff.y, clicks=1, button='left')

coopButton = pyautogui.locateCenterOnScreen('Assets/CoopButton.PNG', confidence=0.9)
if coopButton:
    pyautogui.click(x=coopButton.x, y=coopButton.y, clicks=1, button='left')


recruitButton = pyautogui.locateCenterOnScreen('Assets/RecruitButton.PNG', confidence=0.9)
if recruitButton:
    pyautogui.click(x=recruitButton.x, y=recruitButton.y, clicks=1, button='left')

reqBackupButton = pyautogui.locateCenterOnScreen('Assets/ReqBackupButton.PNG', confidence=0.7)
print(reqBackupButton)
if reqBackupButton:
    pyautogui.click(x=reqBackupButton.x, y=reqBackupButton.y, clicks=1, button='left')