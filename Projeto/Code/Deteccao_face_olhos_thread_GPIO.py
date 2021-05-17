import os
import cv2
import sys
import RPi.GPIO as GPIO
import numpy as np
import time
import threading
from threading import Thread

#Configuracao da porta GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)  
GPIO.setup(7, GPIO.OUT) # pino 7 como saida

# Definindo variaveis globais

# Valores padrao da biblioteca para reconhecimento
cascPath_face = os.getcwd()+'/haarcascades/haarcascade_frontalface_default.xml'
cascPath_eye = os.getcwd()+'/haarcascades/haarcascade_eye.xml'

# Criar interfaces
faceCascade = cv2.CascadeClassifier(cascPath_face)
eyeCascade = cv2.CascadeClassifier(cascPath_eye)
         
def mostrar():
        if format(len(faces)) == '1':
            print("{0} rosto".format(len(faces)))
        else:    
            print("{0} rostos".format(len(faces)))

        if format(len(eyes)) != '0':
            print("{0} olhos".format(len(eyes)))              
        elif format(len(eyes)) == '1':
            print("{0} olho".format(len(eyes)))
        elif format(len(eyes)) == '0':
            print("Nenhum olho encontrado")

def imagem_reconhecida():            
        # Mostrar imagem com os retangulos e deletar a imagem 
        cv2.imshow("rostos e olhos econtrados", image)
        os.system('rm image.jpg')

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
    # Fotografar o rosto com a webcam
    os.system('fswebcam -r 1280x720 image.jpg')
    # Imagem a ser lida
    imagePath = 'image.jpg'
    image = cv2.imread(imagePath)
    # Detectar rosto   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.cv.CV_HAAR_SCALE_IMAGE
            )
    
    # Desenhar retangulos em volta do rosto    
    for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = image[y:y+h, x:x+w]
                
    # Detectar olhos
    eyes = eyeCascade.detectMultiScale(roi_gray, minSize=(30,30))
            
    # Desenhar retangulos em volta dos olhos   
    for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_gray, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    mostrar()
    
    if format(len(faces)) == '0':
            print("Nenhum rosto encontrado".format(len(eyes)))
            if __name__=='__main__':

                    # Sincronizar a thread com a funcao principal  
                    threadLock = threading.Lock()
                    thread = []
                    
                    # Definir funcao alvo
                    thread1 = Thread(target = alerta)
    
                    # Iniciar thread
                    thread1.start()
                    thread.append(thread1)
      
                    #Esperando a thread finalizar
                    thread1.join()


#imagem_reconhecida()

# Press 0 to exit
cv2.waitKey(0)
cv2.destroyAllWindows()
