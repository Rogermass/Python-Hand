import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import threading
import math
#Resolution: 720 x 1280

cap = cv2.VideoCapture(0)

detector = HandDetector(maxHands=1, detectionCon=0.7)
length = 0

fingerpos = [1,1,1,1,1]


(0.1)
    
def index(img):
    
    lil, info, img = detector.findDistance(lmlist1[8], lmlist1[5], img)
    #print(int(lil), "lil")
    lib, info, img = detector.findDistance(lmlist1[6], lmlist1[5], img)
    #print(int(lib), "lib")
    lit, info, img = detector.findDistance(lmlist1[8], lmlist1[6], img)
    #print(int(lit), "lit")
    
    index_angle = (lib**2 + lit**2 - lil**2) / (2 * lib * lit)
    #print(index_angle)
    index_angle = math.degrees(math.acos(index_angle))
    return int(index_angle)

def middle(img):
    lml, info, img = detector.findDistance(lmlist1[12], lmlist1[9], img)
    #print(int(lil), "lil")
    lmb, info, img = detector.findDistance(lmlist1[12], lmlist1[10], img)
    #print(int(lib), "lib")
    lmt, info, img = detector.findDistance(lmlist1[10], lmlist1[9], img)
    #print(int(lit), "lit")
    
    middle_angle = (lmb**2 + lmt**2 - lml**2) / (2 * lmb * lmt)
    #print(index_angle)
    middle_angle = math.degrees(math.acos(middle_angle))
    return int(middle_angle)

def ring(img):

    lrl, info, img = detector.findDistance(lmlist1[16], lmlist1[13], img)
    #print(int(lil), "lil")
    lrb, info, img = detector.findDistance(lmlist1[16], lmlist1[14], img)
    #print(int(lib), "lib")
    lrt, info, img = detector.findDistance(lmlist1[14], lmlist1[13], img)
    #print(int(lit), "lit")
    
    ring_angle = (lrb**2 + lrt**2 - lrl**2) / (2 * lrb * lrt)
    #print(index_angle)
    ring_angle = math.degrees(math.acos(ring_angle))
    return int(ring_angle)

def pinky(img):
    lpl, info, img = detector.findDistance(lmlist1[20], lmlist1[17], img)
    #print(int(lil), "lil")
    lpb, info, img = detector.findDistance(lmlist1[20], lmlist1[18], img)
    #print(int(lib), "lib")
    lpt, info, img = detector.findDistance(lmlist1[18], lmlist1[17], img)
    #print(int(lit), "lit")
    
    pinky_angle = (lpb**2 + lpt**2 - lpl**2) / (2 * lpb * lpt)
    #print(index_angle)
    pinky_angle = math.degrees(math.acos(pinky_angle))
    return int(pinky_angle)

def thumb(img):
    ltl, info, img = detector.findDistance(lmlist1[4], lmlist1[2], img)
    #print(int(lil), "lil")
    ltb, info, img = detector.findDistance(lmlist1[4], lmlist1[3], img)
    #print(int(lib), "lib")
    ltt, info, img = detector.findDistance(lmlist1[3], lmlist1[2], img)
    #print(int(lit), "lit")
    
    thumb_angle = (ltb**2 + ltt**2 - ltl**2) / (2 * ltb * ltt)
    #print(index_angle)
    thumb_angle = math.degrees(math.acos(thumb_angle))
    return int(thumb_angle)

def data(img):
        
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
        
        #data(img)
        print(str(thumb(img)) + ", " + str(index(img)) + ", " + str(middle(img)) + ", " + str(ring(img)) + ", " + str(pinky(img)))
            
    cv2.imshow("Image", img)
    cv2.waitKey(1) 
    if cv2.waitKey(1) == ord("q"):
        break
    

cap.release()
cv2.destroyAllWindows()