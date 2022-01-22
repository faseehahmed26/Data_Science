import cv2
import mediapipe as mp
import time


class FaceMeshDetector():
    def __init__(self,staticMode=False,maxFaces=2,refine_landmarks=False,minDetectionCon=0.5,minTrackCon=0.5):
        self.staticMode=staticMode
        self.maxFaces=maxFaces
        self.refine_landmarks=refine_landmarks
        self.minDetectionCon=minDetectionCon
        self.minTrackCon=minTrackCon

        self.mpDraw=mp.solutions.drawing_utils
        self.mpFaceMesh=mp.solutions.face_mesh
        self.faceMesh=self.mpFaceMesh.FaceMesh(self.staticMode,self.maxFaces,self.refine_landmarks,self.minDetectionCon,self.minDetectionCon)
        self.faceMeshDraw=mp.solutions.face_mesh_connections
        self.drawSpec=self.mpDraw.DrawingSpec(color=(0,255,0),thickness=1,circle_radius=1)

    def findFaceMesh(self,img,draw=True):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results=self.faceMesh.process(imgRGB)
        faces=[]
        if results.multi_face_landmarks:
           
            for faceLms in results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,faceLms,self.faceMeshDraw.FACEMESH_TESSELATION,self.drawSpec,self.drawSpec)
                    
                    face=[]
                for id,lm in enumerate(faceLms.landmark):
                # print(lm)
                    ih,iw,ic=img.shape
                    x,y=int(lm.x*iw),int(lm.y*ih)
                    #cv2.putText(img,str(id),(x,y),cv2.FONT_HERSHEY_PLAIN,0.7,(0,255,0),1)
                    #print(id,x,y)
                    face.append([x,y])
                faces.append(face)
        return img,faces
def main():
    cap=cv2.VideoCapture('PoseVideos/1.mp4')
    pTime=0
    detector=FaceMeshDetector(maxFaces=1)
    while True:
        success, img=cap.read()
        img,faces=detector.findFaceMesh(img)
        if len(faces)!=0:
            print(len(faces))
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,f'FPS:{int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)
        cv2.imshow('Image',img)
        a=cv2.waitKey(1)
        if a==ord('q'):
            break

   
   



if __name__ == '__main__':
    main()