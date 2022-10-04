import pyautogui
import math
print('Press Ctrl-C to quit.')
pyautogui.FAILSAFE = False
x,y =pyautogui.size()
R=400
X=x/2
Y=y/2
pyautogui.moveTo(X+R,Y)
pyautogui.Pause = 0
while True:
    for i in range(360):
        if i%6==0:
            pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))

