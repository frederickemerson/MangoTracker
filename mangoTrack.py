import cv2
import numpy as np

mango=[]
cap = cv2.VideoCapture("mangoes.mp4")
out = cv2.VideoWriter("outputm.mp4",cv2.VideoWriter_fourcc(*'MP4V'),10,(640,352))

while cap.isOpened():
    ret,frame = cap.read()
  
    if ret is False:
        break

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_hue=np.array([19,60,60])
    upper_hue=np.array([23,255,255])
    mask = cv2.inRange(hsv,lower_hue,upper_hue)

    (contours,_) = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    center = None

    if len(contours)>0:
        c = max(contours,key=cv2.contourArea)
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        try:
            center = (int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
            cv2.circle(frame,center,10,(255,0,0),-1)
            mango.append(center)
        except:
           pass   
        if len(mango)>2:
            for i in range(1,len(mango)):
                cv2.line(frame,mango[i-1],mango[i],(0,0,255),5)
                #cv2.imshow('fr',frame)
    out.write(frame)
print("Written Sucessfully")
out.release()
cap.release()

