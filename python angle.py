import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import threading
import math
#Resolution: 720 x 1280

cap = cv2.VideoCapture(0)

detector = HandDetector(maxHands=1, detectionCon=0.7)
    
def index(img):
    
    lil, info, img = detector.findDistance(lmlist1[8], lmlist1[5], img)
    
    lib, info, img = detector.findDistance(lmlist1[6], lmlist1[5], img)
    
    lit, info, img = detector.findDistance(lmlist1[8], lmlist1[6], img)
    
    
    index_angle = (lib**2 + lit**2 - lil**2) / (2 * lib * lit)
    
    index_angle = math.degrees(math.acos(index_angle))
    return int(index_angle)

def middle(img):
    lml, info, img = detector.findDistance(lmlist1[12], lmlist1[9], img)
    
    lmb, info, img = detector.findDistance(lmlist1[12], lmlist1[10], img)
    
    lmt, info, img = detector.findDistance(lmlist1[10], lmlist1[9], img)
    
    
    middle_angle = (lmb**2 + lmt**2 - lml**2) / (2 * lmb * lmt)

    middle_angle = math.degrees(math.acos(middle_angle))
    return int(middle_angle)

def ring(img):

    lrl, info, img = detector.findDistance(lmlist1[16], lmlist1[13], img)
    
    lrb, info, img = detector.findDistance(lmlist1[16], lmlist1[14], img)
    
    lrt, info, img = detector.findDistance(lmlist1[14], lmlist1[13], img)
    
    
    ring_angle = (lrb**2 + lrt**2 - lrl**2) / (2 * lrb * lrt)
    
    ring_angle = math.degrees(math.acos(ring_angle))
    return int(ring_angle)

def pinky(img):
    lpl, info, img = detector.findDistance(lmlist1[20], lmlist1[17], img)
    
    lpb, info, img = detector.findDistance(lmlist1[20], lmlist1[18], img)
    
    lpt, info, img = detector.findDistance(lmlist1[18], lmlist1[17], img)
    
    
    pinky_angle = (lpb**2 + lpt**2 - lpl**2) / (2 * lpb * lpt)
    
    pinky_angle = math.degrees(math.acos(pinky_angle))
    return int(pinky_angle)

def thumb(img):
    ltl, info, img = detector.findDistance(lmlist1[4], lmlist1[2], img)
    
    ltb, info, img = detector.findDistance(lmlist1[4], lmlist1[3], img)
    
    ltt, info, img = detector.findDistance(lmlist1[3], lmlist1[2], img)
    
    
    thumb_angle = (ltb**2 + ltt**2 - ltl**2) / (2 * ltb * ltt)
    
    thumb_angle = math.degrees(math.acos(thumb_angle))
    return int(thumb_angle)

def data(img):
    #77, 8, 15, 18, 29
    
    thumbangle = int((thumb(img) * 60) / 180)
    indexangle = int((index(img) * 130) / 180)
    middleangle = int((middle(img) * 100) / 180)
    ringangle = int((ring(img) * 130) / 180)
    pinkyangle = int((pinky(img) * 100) / 180)
    
    arduino_angles = [thumbangle, indexangle, middleangle, ringangle, pinkyangle]    
    print(arduino_angles)
    print(str(thumb(img)) + ", " + str(index(img)) + ", " + str(middle(img)) + ", " + str(ring(img)) + ", " + str(pinky(img)))
    time.sleep(0.5)                

threading.Thread(target=data).start()    

while True:
    success, img = cap.read()
    #img = cv2.resize(img, (640, 420)) 
    hands, img = detector.findHands(img)
    
    #print('Resolution: ' + str(img.shape[0]) + ' x ' + str(img.shape[1]))
    if hands:
        hand1 = hands[0]
        lmlist1 = hand1["lmList"]
        bbox = hand1["bbox"]
        cp1 = hand1["center"]
        HandType = hand1["type"]
        
        data(img)
        #print(str(thumb(img)) + ", " + str(index(img)) + ", " + str(middle(img)) + ", " + str(ring(img)) + ", " + str(pinky(img)))
            
    cv2.imshow("Hand Processor", img)
    cv2.waitKey(1) 
    if cv2.waitKey(1) == ord("q"):
        break
    

cap.release()
cv2.destroyAllWindows()