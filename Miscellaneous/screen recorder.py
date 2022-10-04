import cv2
import numpy as np
from PIL import ImageGrab
import time
time.sleep(4)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
filename='output'+str(time.time())+".avi"
out=cv2.VideoWriter(filename,fourcc,15.0,(1366,768))

while True:
    img=ImageGrab.grab()
    img_np=np.array(img)
    frame=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    out.write(frame)

    if cv2.waitKey(1)==36:
        break
out.release()
cv2.destroyAllWindows()
