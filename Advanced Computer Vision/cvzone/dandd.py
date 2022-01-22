import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import numpy as np

cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector=HandDetector(detectionCon=0.8,maxHands=1)
colorR=(255,0,255)
cx,cy,w,h=100,100,200,200


class DragRect():
    def __init__(self,posCenter,size=[200,200]):
        self.posCenter=posCenter
        self.size=size
    
    def update(self,cursor):
        cx,cy=self.posCenter
        w,h=self.size

        #If the index finger tip is in renctangle region
        if cx-w//2<cursor[0]<cx+w//2 and cy-h//2<cursor[1]<cy+h//2:
                colorR=0,255,0
                self.posCenter=cursor

rectList=[]
for x in range(5):
    rectList.append(DragRect([x * 250 + 150,150]))

while True:
  
    success,img=cap.read()
    hands,img=detector.findHands(img)
    if hands:
        # Hand 1
        # Hand -dict(lmList-bbox-center-type)
        hand1=hands[0]
        lmList1=hand1['lmList'] #List of 21  Landmark Points
        #hand2=hands[1]
        #lmList2=hand2['lmList'] #List of 21  Landmark Points
        #if lmList1:
        l,_,_= detector.findDistance(lmList1[8],lmList1[12],img)
        print(l)
        if l < 40:
            cursor=lmList1[8] #Index Finger tip Landmark
            #Call the Update Here
            for rect in rectList:
                rect.update(cursor)
        #print(len(lmList1),lmList1)
        #print(lmList1[8])
    
    ##Draw solid
    #for rect in rectList:
    #    cx,cy=rect.posCenter
    #    w,h=rect.size
    #    cv2.rectangle(img,(cx - w //2,cx - h //2),(cx + w //2,cx + h //2),colorR,cv2.FILLED)
    #    cvzone.cornerRect(img,(cx - w //2,cx - h //2,w,h),20,rt=0)

    #Draw Transparent
    imgNew=np.zeros_like(img,np.uint8)
    for rect in rectList:
       cx,cy=rect.posCenter
       w,h=rect.size
       cv2.rectangle(imgNew,(cx - w //2,cx - h //2),(cx + w //2,cx + h //2),colorR,cv2.FILLED)
       cvzone.cornerRect(imgNew,(cx - w //2,cx - h //2,w,h),20,rt=0)

    out=img.copy()
    alpha=0.5
    mask=imgNew.astype(bool)
    out[mask]=cv2.addWeighted(img,alpha,imgNew,1-alpha,0)[mask]
    
    cv2.imshow("Image",out)
    cv2.waitKey(1)