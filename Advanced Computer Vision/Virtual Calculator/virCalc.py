import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep

class Button():
    def __init__(self,pos,width,height,value):
        self.pos=pos
        self.width=width
        self.height=height
        self.value=value
    def draw(self,img):
        cv2.rectangle(img,self.pos,(self.pos[0]+self.width,self.pos[1]+self.height),(225,225,225),cv2.FILLED)
        cv2.rectangle(img,self.pos,(self.pos[0]+self.width,self.pos[1]+self.height),(50,50,50),3)
        cv2.putText(img,self.value,(self.pos[0]+40,self.pos[1]+60),cv2.FONT_HERSHEY_PLAIN,2,(50,50,50),2)

    def checkClick(self,x,y):
        if self.pos[0]<x<self.pos[0]+self.width and self.pos[1]<y<self.pos[1]+self.height:
            cv2.rectangle(img,self.pos,(self.pos[0]+self.width,self.pos[1]+self.height),(255,255,255),cv2.FILLED)
            cv2.rectangle(img,self.pos,(self.pos[0]+self.width,self.pos[1]+self.height),(50,50,50),3)
            cv2.putText(img,self.value,(self.pos[0]+25,self.pos[1]+80),cv2.FONT_HERSHEY_PLAIN,5,(0,0,0),5)
            return True
        else:
            False

#Webcam
cap=cv2.VideoCapture(0)
cap.set(3,1280)#width
cap.set(4,720)#height
#hand Detection
detector=HandDetector(detectionCon=0.8,maxHands=1)
#Creatung Buttons
buttonListvalues=[['7','8','9','*'],
                  ['4','5','6','-'],
                  ['1','2','3','+'],
                  ['0','/','.','=']]
buttonList=[]
for x in range(4):
    for y in range(4):
        xpos=x*100+800
        ypos=100*y+150
        buttonList.append(Button((xpos,ypos),100,100,buttonListvalues[y][x]))
#variables
myEquation=""
delayCounter=0
#loop
while True:
    #Get Image From Webcam
    success,img=cap.read()
    img=cv2.flip(img,1)
    #Detection
    hands,img=detector.findHands(img,flipType=False)
    #Draw All buttons
    cv2.rectangle(img,(800,50),(800+400,70+100),(225,225,225),cv2.FILLED)
    cv2.rectangle(img,(800,50),(800+400,70+100),(50,50,50),3)
    

    for but in buttonList:
        but.draw(img)
    #Check for hands:
    if hands:
        lmList=hands[0]['lmList']
        
        l,_,img=detector.findDistance(lmList[8],lmList[12],img)
        #print(l)
        x,y=lmList[8]
        if l<52:
            for i,but in enumerate(buttonList):
                if but.checkClick(x,y) and delayCounter==0:
                    val=buttonListvalues[int(i%4)][int(i/4)]
                    #sleep(0.5)
                    if val == "=":
                        myEquation=str(eval(myEquation))
                    else:
                        myEquation+=val
                    delayCounter=1
    #Avoid Duplicates
    if delayCounter!=0:
        delayCounter+=1
        if delayCounter>10:
            delayCounter=0
    #Display the Calculation
    cv2.putText(img,myEquation,(810,120),cv2.FONT_HERSHEY_PLAIN,3,(50,50,50),3)

   
    #Display Image
    cv2.imshow("Calculator",img)
    a=cv2.waitKey(1)
    
    if a==ord('q'):
        break
    elif a==ord('c'):
        myEquation=''