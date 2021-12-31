import cv2
from cvzone.HandTrackingModule import HandDetector
import time


cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.7)
length = 0


def data(thumb, index, middle, ring, pinky):
    
    #thumb = int(thumb)
    index = int(index)
    middle = int(middle)
    ring = int(ring)
    pinky = int(pinky)
    
    fingerpos = [thumb, index, middle, ring, pinky]
    print(tuple(fingerpos))
    time.sleep(1)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    
    if hands:
        hand1 = hands[0]
        lmlist1 = hand1["lmList"]
        bbox = hand1["bbox"]
        cp1 = hand1["center"]
        HandType = hand1["type"]
        
        
        length_thumb = detector.fingersUp(hand1)
        length_thumb = length_thumb[0]
        
        length_index, info, img = detector.findDistance(lmlist1[8], lmlist1[5], img)
        
        length_middle, info, img = detector.findDistance(lmlist1[12], lmlist1[9], img)
        
        length_ring, info, img = detector.findDistance(lmlist1[16], lmlist1[13], img)
        
        length_pinky, info, img = detector.findDistance(lmlist1[20], lmlist1[17], img)
        
        data(length_thumb, length_index, length_middle, length_ring, length_pinky)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1) 
    if cv2.waitKey(1) == ord("q"):
        break
    

cap.release()
cv2.destroyAllWindows()