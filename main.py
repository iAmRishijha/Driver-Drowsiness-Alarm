
import numpy as np
import cv2 as cv
import dlib
from imutils import face_utils
import pygame

pygame.init()
drowsy = pygame.mixer.Sound("media\drowsy.mp3")
sleepy = pygame.mixer.Sound("media\sleepy.mp3")

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def distance(x,y):
    return np.linalg.norm(x-y)

def checkBlink(a,b,c,d,e,f):
    up = distance(b,f)+distance(c,e)
    side = distance(a,d)
    ear = up/(2.0*side)

    if ear>0.25:
        return 2
    elif ear>0.21 and ear<=0.25:
        return 1
    return 0

awake_count = 0
sleepy_count = 0
drowsy_count = 0
status = ""

video = cv.VideoCapture(0)
while True:
    ret,frame = video.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv.rectangle(frame,(x1,y1),(x2,y2),(0,255,0), 1)

        landmarks = predictor(frame,face)
        landmarks = face_utils.shape_to_np(landmarks)

        left_eye = checkBlink(landmarks[36],landmarks[37],landmarks[38],landmarks[39],landmarks[40],landmarks[41])
        right_eye = checkBlink(landmarks[42],landmarks[43],landmarks[44],landmarks[45],landmarks[46],landmarks[47])

        if left_eye ==2 or right_eye ==2:
            sleepy_count+=1
            awake_count = 0
            drowsy_count = 0
            if sleepy_count>2:
                status = "Awake"
                sleepy.stop()
                drowsy.stop()

        elif left_eye == 1 or right_eye == 1:
            awake_count = 0
            sleepy_count = 0
            drowsy_count += 1
            if drowsy_count>5:
                status = "Drowsy"
                sleepy.stop()
                drowsy.play()
        else:
            awake_count += 1
            sleepy_count = 0
            drowsy_count = 0
            if awake_count>5:
                status = "Sleepy"
                drowsy.stop()
                sleepy.play()

        cv.putText(frame, status, (100,100), cv.FONT_HERSHEY_DUPLEX, 1.2, (255,255,255),3)
    cv.imshow("video",frame)

    if cv.waitKey(1) & 0xff == ord('q'):
        break

video.release()
cv.destroyAllWindows()

