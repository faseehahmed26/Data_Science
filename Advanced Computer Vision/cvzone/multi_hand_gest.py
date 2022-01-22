import cv2
from cvzone.HandTrackingModule import HandDetector


cap=cv2.VideoCapture(0)
detector=HandDetector(detectionCon=0.8,maxHands=2)

while True:
    success,img=cap.read()
   #hands,img=detector.findHands(img,flipType=False) #for flipping right 
    hands,img=detector.findHands(img)
    if hands:
        # Hand 1
        # Hand -dict(lmList-bbox-center-type)
        hand1=hands[0]
        lmList1=hand1['lmList'] #List of 21  Landmark Points
        bbox1=hand1['bbox'] #Bounding Box info x,y,w,h
        centerPoint1=hand1['center'] # Center of the hand cx,cy
        handType1=hand1["type"] #Hand Type Left Or Right    
        fingers1=detector.fingersUp(hand1) #How many fingers are up
        #length,info,img=detector.findDistance(lmList1[8],lmList1[12],img) #For Drawing
        #length,info=detector.findDistance(lmList1[8],lmList1[12]) #For not draing it 
        #print(len(lmList1),lmList1)
        #print(bbox1)
        if len(hands)==2:
            hand2=hands[1]
            lmList2=hand2['lmList'] #List of 21  Landmark Points
            bbox2=hand2['bbox'] #Bounding Box info x,y,w,h
            centerPoint2=hand2['center'] # Center of the hand cx,cy
            handType2=hand2["type"] #Hand Type Left Or Right    
            
            fingers2=detector.fingersUp(hand2)
           # length,info,img=detector.findDistance(lmList1[8],lmList2[8],img) 
            length,info,img=detector.findDistance(centerPoint1,centerPoint2,img) 
            #print(fingers1,fingers2)

    cv2.imshow("Image",img)
    cv2.waitKey(1)


