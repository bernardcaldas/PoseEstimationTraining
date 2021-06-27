import numpy as np
import cv2
import time


wCam, hCam = 640,480

cap = cv2.VideoCapture('boxing.mp4')
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0

while True:
    success, img = cap.read()

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (50,70), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,0), 2)
    cv2.imshow(" fps ", img)
    c = cv2.waitKey(1)
    if c == 27:
        break


# release the cap object
cap.release()
# close all windows
cv2.destroyAllWindows()    