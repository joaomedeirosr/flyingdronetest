from djitellopy import tello
import cv2 as cv
import cvzone
from cvzone.FaceDetectionModule import FaceDetector




webcam = cv.VideoCapture(0)
detector = FaceDetector()

_,img = webcam.read()
hi,wi,_ = img.shape

#                  P I D
xPID = cvzone.PID([1,0,0], wi//2 )



#drone = tello.Tello()
#drone.connect()

#print(drone.get_battery())
#drone.streamoff()
#drone.streamon()

while True:
    _,img = webcam.read()
    #img = drone.get_freame_read().frame
    img,bboxs = detector.findFaces(img,draw=True)

    if bboxs:
        cx,cy = bboxs[0]['center']

        xVal = int(xPID.update(cx))

        img = xPID.draw(img,[cx,cy])


                        #### --> Calc for find center the image and draw <---- ######

        #cv.putText(img, str(xVal), (50,100), cv.FONT_HERSHEY_PLAIN,3 (255,255,0),3)

        #cv.circle(img,(cx,cy),5,(255,255,0),cv.FILLED)
        #cv.line(img,(wi//2,0),(wi//2,hi),(255,255,0),1)

        #error = wi//2 - cx
        #cv.putText(img,str(error),(50,100),cv.FONT_HERSHEY_PLAIN,3,(255,255,0),3)
        #cv.line(img,(wi//2,hi//2),(cx,cy),(255,255,0),1)

                        ### --->         END               <----- #####
  

    cv.imshow("Transmissao",img)
    if cv.waitKey(5) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()


