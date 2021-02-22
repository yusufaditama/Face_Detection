import numpy as np
import cv2

#cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3,240) # set Width
cap.set(4,240) # set Height

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,      
        minSize=(30, 30)
    )
    
    
    if len(faces) > 0:
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img, ("1"), (10,40), font, 1, (0,255,0), 2)
            print ("Terdapat", str(len(faces)), "wajah")
            
            roi_gray = gray[y:y+h, x:x+w]
            #roi_color = img[y:y+h, x:x+w]
            
    elif len(faces)  == 0:
        cv2.putText(img, ("0"), (10,40), font, 1, (0,0,255), 2)
        print ("Tak ada wajah")
        
     
    cv2.imshow('video', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
