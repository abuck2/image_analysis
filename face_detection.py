import cv2, time
import numpy as np

img = cv2.imread('faces.jpg')

#Load a pre-trained model
face_cascade = cv2.CascadeClassifier('model.xml')

#Load the image in grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Applay grayscale to cascade class : object, #of detection
boxes, detections = face_cascade.detectMultiScale2(gray)


print(boxes) #4 lignes = 4 visages
print(detections)  # We need to find a threshold of minN (6 for ex)
boxes, detections = face_cascade.detectMultiScale2(gray, minNeighbors=6)
