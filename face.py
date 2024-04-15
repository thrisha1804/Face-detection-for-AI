import cv2

algorithm = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(algorithm)

camera = cv2.VideoCapture(0)

while True:
    _,img = camera.read()
    grayImg =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayImg,1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h) ,(255,255,255),2)
    cv2.imshow("FaceDetection",img)
    keyboard = cv2.waitKey(10)
    if keyboard == 27:
        break
camera.release()
cv2.destroyAllWindows()
    
