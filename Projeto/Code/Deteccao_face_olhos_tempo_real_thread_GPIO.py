import os
import cv2
import sys
import RPi.GPIO as GPIO
import numpy as np
import time
import threading
from threading import Thread

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)  
GPIO.setup(7, GPIO.OUT) # pino 7 como saida

cascPath_face = os.getcwd()+'/haarcascades/haarcascade_frontalface_alt.xml'
cascPath_eye = os.getcwd()+'/haarcascades/haarcascade_eye.xml'
faceCascade = cv2.CascadeClassifier(cascPath_face)
eyeCascade = cv2.CascadeClassifier(cascPath_eye)

video_capture = cv2.VideoCapture(0)

def mostrar():
        if format(len(faces)) == '1':
            print("{0} rosto".format(len(faces)))
        else:    
            print("{0} rostos".format(len(faces)))

       # if format(len(eyes)) != '0':
       #     print("{0} olhos".format(len(eyes)))              
       # elif format(len(eyes)) == '1':
       #     print("{0} olho".format(len(eyes)))
       # elif format(len(eyes)) == '0':
       #     print("Nenhum olho encontrado")

def alerta():
        i=0
        blink=10
        while (i < blink):
                GPIO.setup (7, GPIO.OUT)
                GPIO.output (7, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output (7, GPIO.LOW)
                time.sleep(0.1)
                i=i+1
        return;

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eyeCascade.detectMultiScale(roi_gray, minSize=(30,30))
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_gray, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)
 
    mostrar()

    if format(len(faces)) == '0':
        print("Nenhum rosto encontrado".format(len(faces)))
        if __name__=='__main__':

            # Sincronizar a thread com a funcao principal  
            threadLock = threading.Lock()
            thread = []
                    
            # Definir funcao alvo
            thread1 = Thread(target = alerta)
    
            # Iniciar thread
            thread1.start()
            thread.append(thread1)
      
            # Esperando a thread finalizar
            thread1.join()

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        GPIO.cleanup()
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
