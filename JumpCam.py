import cv2
from numpy import array
from keyboard import press_and_release as press
from time import sleep as sl
 
#   Inner rectangle coordinates 
x1 = 120
y1 = 90
x2 = 525
y2 = 405

#   Czpture from camera Number 0 with a resolution of 640*480
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    _, frame = cap.read()
    #   Color encoding parameters
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #   The range of accepted reds
    lred = array([0, 200, 90])
    ured = array([30, 255, 255])
    #   Create a mask for the accepted rnage of reds
    mask = cv2.inRange(hsv, lred, ured)
    #   Apply the mask to the recorded frame
    res = cv2.bitwise_and(frame, frame, mask=mask)
    #   Draw a green rectanble on the frame (Area where the mask applies)
    cv2.rectangle(frame, (x1, y1), (x2, y2), (30, 210, 10), 2)
    #   Crop the frame where the rectangle is drawn
    cropped = mask[y1+5:y2-5, x1+5:x2-5]
    #   If there are more than 60 non black pixels on the mask press Space
    if cv2.countNonZero(cropped) > 60:
        press('space')
    #   Show the frames
    cv2.imshow('Mausk', cropped)
    cv2.imshow('frame', frame)
    #   Quit if X is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
