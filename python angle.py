import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import threading
import math

def index():
    
    lil, info = detector.findDistance(lmlist1[8], lmlist1[5])
    
    lib, info = detector.findDistance(lmlist1[6], lmlist1[5])
    
    lit, info = detector.findDistance(lmlist1[8], lmlist1[6])
    
    
    index_angle = (lib**2 + lit**2 - lil**2) / (2 * lib * lit)
    
    index_angle = math.degrees(math.acos(index_angle))
    
    index_angle = 180 - index_angle
    return int(index_angle)

def middle():
    lml, info = detector.findDistance(lmlist1[12], lmlist1[9])
    
    lmb, info = detector.findDistance(lmlist1[12], lmlist1[10])
    
    lmt, info = detector.findDistance(lmlist1[10], lmlist1[9])
    
    
    middle_angle = (lmb**2 + lmt**2 - lml**2) / (2 * lmb * lmt)

    middle_angle = math.degrees(math.acos(middle_angle))
    
    middle_angle = 180 - middle_angle
    return int(middle_angle)

def ring():

    lrl, info = detector.findDistance(lmlist1[16], lmlist1[13])
    
    lrb, info = detector.findDistance(lmlist1[16], lmlist1[14])
    
    lrt, info = detector.findDistance(lmlist1[14], lmlist1[13])
    
    
    ring_angle = (lrb**2 + lrt**2 - lrl**2) / (2 * lrb * lrt)
    
    ring_angle = math.degrees(math.acos(ring_angle))
    
    ring_angle = 180 - ring_angle
    return int(ring_angle)

def pinky():
    lpl, info = detector.findDistance(lmlist1[20], lmlist1[17])
    
    lpb, info = detector.findDistance(lmlist1[20], lmlist1[18])
    
    lpt, info = detector.findDistance(lmlist1[18], lmlist1[17])
    
    
    pinky_angle = (lpb**2 + lpt**2 - lpl**2) / (2 * lpb * lpt)
    
    pinky_angle = math.degrees(math.acos(pinky_angle))
    
    pinky_angle = 180 - pinky_angle
    return int(pinky_angle)

def thumb():
    ltl, info = detector.findDistance(lmlist1[4], lmlist1[2])
    
    ltb, info = detector.findDistance(lmlist1[4], lmlist1[3])
    
    ltt, info = detector.findDistance(lmlist1[3], lmlist1[2])
    
    
    thumb_angle = (ltb**2 + ltt**2 - ltl**2) / (2 * ltb * ltt)
    
    thumb_angle = math.degrees(math.acos(thumb_angle))
    
    thumb_angle = 180 - thumb_angle
    return int(thumb_angle)

def data():
    #77, 8, 15, 18, 29
    
    thumbangle = int((thumb() * 60) / 100)
    indexangle = int((index() * 130) / 180)
    middleangle = int((middle() * 100) / 180)
    ringangle = int((ring() * 130) / 180)
    pinkyangle = int((pinky() * 100) / 180)
    
    arduino_angles = [thumbangle, indexangle, middleangle, ringangle, pinkyangle]    
    print(arduino_angles)
    print(str(thumb()) + ", " + str(index()) + ", " + str(middle()) + ", " + str(ring()) + ", " + str(pinky()))
                
  
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.7)

start = time.time()
while True:
    success, img = cap.read()
 
    hands, img = detector.findHands(img)

    if hands:
        hand1 = hands[0]
        lmlist1 = hand1["lmList"]
        bbox = hand1["bbox"]
        cp1 = hand1["center"]
        HandType = hand1["type"]
        
    

        current_time = time.time()
        if current_time - start >= 0.5:
            data()
            start = current_time
            
    cv2.imshow("Hand Processor", img)
    cv2.waitKey(1) 
    if cv2.waitKey(1) == ord("q"):
        break
    

cap.release()
cv2.destroyAllWindows()