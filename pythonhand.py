import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.7)

while True:
    success, img = cap.read()
    img = detector.findHands(img)

    cv2.imshow("Image", img[1])
    
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()