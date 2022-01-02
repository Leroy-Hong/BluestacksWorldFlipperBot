import pyautogui


bossBattleButton = pyautogui.locateCenterOnScreen('Assets/BossBattlesButton.PNG', confidence=0.9)
if bossBattleButton:
    pyautogui.click(x=bossBattleButton.x, y=bossBattleButton.y, clicks=1, button='left')