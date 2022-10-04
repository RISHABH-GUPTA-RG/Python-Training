import pyautogui
while True:
    x, y = pyautogui.position()
    positionStr = 'X: ' + str(x) + ' Y: ' + str(y).rjust(4)
    print(positionStr)
