import cv2
from random import randrange

#load some pre-trained data on face frontal from opencv(haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choose image or video to detect face in
img = cv2.imread('big_crowd.png')

##To capture from a video/webcam
#webcam = cv2.VideoCapture(0'file.mp4' or videoinputpath)

##while loop to iterate through all video frames
#while True:
    ##read current frames
    #successful_frame_read, frame = webcam.read()

    ##Must convert to grayscale
    #grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ##detect faces
    #face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    ##draw rectangle around faces
    #for (x, y, w, h) in face_coordinates:
        #cv2.rectangle(frame, (x,y), (x+w, y+h), (256), (256), (256), 5)

    #cv2.imshow('Face Detector', frame)
    #key = cv2.waitKey(1)

    ##break out of infinite loop
    #if key == 81 or key == 113:
    #   break

##Release the VideoCapture object
#webcam.release()


#make img grayscale-remove rgb values from pixels
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#draw rectangle around faces
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x,y), (x+w, y+h), (randrange(128, 256), randrange(128, 256), randrange(128, 256)), 2)

#display image w/ faces
cv2.imshow('Face Detector', img)
cv2.waitKey()

print("Code Completed")
