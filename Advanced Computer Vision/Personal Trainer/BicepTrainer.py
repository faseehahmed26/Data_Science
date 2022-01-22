import cv2
import time
import PoseModule as pm
import os
import numpy as np

#Video
wCam,hCam=640,480

cap=cv2.VideoCapture('PoseVideos/7.mp4')
cap.set(3,wCam)
cap.set(4,hCam)
dir=0
count=0
#Image
#img=cv2.imread("PoseVideos/test.jpeg")


#Detector
detector=pm.poseDetector()

pTime=0
while True:
    success,img=cap.read()
    #img=cv2.imread("PoseVideos/test.jpeg")
    img=cv2.resize(img,(1280,720))
    img=detector.findPose(img,False)
    lmList=detector.findPosition(img,False)
    if len(lmList)!=0:
        #Right Arm
        angle=detector.findAngle(img,12,14,16)
        #Left Arm
        #angle=detector.findAngle(img,11,13,15)
    
        per=np.interp(angle,(160,40),(0,100))
        bar=np.interp(angle,(160,40),(650,100))
        print(per,angle)

        #Check for the dubmbell curls
        color = (255, 0, 255)
        if per == 100:
            color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            color = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0
        print(count)
        
        #Draw Bar
        cv2.rectangle(img,(1100,100),(1175,650),color,3)
        cv2.rectangle(img,(1100,int(bar)),(1175,650),color,cv2.FILLED)
        cv2.putText(img,f'{int(per)} %',(1100,75),cv2.FONT_HERSHEY_PLAIN,4,color,4)
        
        #Draw Curl Count
        cv2.rectangle(img,(0,450),(250,720),(0,255,0),cv2.FILLED)
        cv2.putText(img,f'{int(count)}',(45,670),cv2.FONT_HERSHEY_PLAIN,15,(255,0,0),25)
    
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,f'FPS :{int(fps)}',(50,100),cv2.FONT_HERSHEY_PLAIN,5,(255,0,0),5)
    cv2.imshow("Trainer",img)
    a=cv2.waitKey(1)
    if a==ord('q'):
        break
