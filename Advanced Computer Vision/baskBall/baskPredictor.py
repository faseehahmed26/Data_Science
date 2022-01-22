import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np
import math
#Initialize the video
cap=cv2.VideoCapture('Videos/vid (6).mp4')

#Create the color finder object
colorFinder=ColorFinder(False)
hsvVals= {'hmin': 8, 'smin': 96, 'vmin': 115, 'hmax': 14, 'smax': 255, 'vmax': 255}

#Variables
posListX,posListY=[],[]
xList=[item for item in range(0,1300)]
prediction=False
while True:
    success,img=cap.read()
    #Grab the image
    #img=cv2.imread("Ball.png")
    img=img[0:900,:]
    #Find The colour of Ball
    imgColor,mask=colorFinder.update(img,hsvVals)
    #Find the loaction of Ball
    imgContours,contours=cvzone.findContours(img,mask,minArea=500)
    if contours:
        
        posListX.append(contours[0]['center'][0])
        posListY.append(contours[0]['center'][1])
    if posListX and posListY:
        # Polynomial Regression y=Ax^2 +Bx+C
        #Find the Coeffcients
        A,B,C=np.polyfit(posListX,posListY ,2)

        for i,(posX,posY) in enumerate(zip(posListX,posListY)):
            pos=(posX,posY)
            cv2.circle(imgContours,pos,10,(0,255,0),cv2.FILLED)
            if i==0:
                cv2.line(imgContours,pos,pos,(0,255,0),5)
            else:
                cv2.line(imgContours,pos,(posListX[i-1],posListY[i-1]),(0,255,0),5)
        
        for x in xList:
            y=int(A*x**2+B*x+C)
            cv2.circle(imgContours,(x,y),2,(255,0,255),cv2.FILLED)
        if len(posListX)<10:
            #Prediction
            #X values 330 to 430
            a=A
            b=B
            c=C-590

            x=int((-b -math.sqrt(b**2-(4*a*c)))/(2*a))
            prediction=330<x<430
        
        if prediction:
            #print(x,"Basket")
            cvzone.putTextRect(imgContours,"Basket",(50,100),scale=7,thickness=5,colorR=(0,255,0),offset=20)

        else:
            #print(x,"No Basket")
            cvzone.putTextRect(imgContours,"No Basket",(50,100),scale=7,thickness=5,colorR=(0,0,255),offset=20)

    #Display
    imgContours=cv2.resize(imgContours,(0,0),None,0.7,0.7)

    #img=cv2.resize(img,(0,0),None,0.7,0.7)
    #cv2.imshow("Basket Ball Short Predictor",img)
    cv2.imshow("Basket Ball Color Predictor",imgContours)

    a=cv2.waitKey(50)
    if a==ord('q'):
        break