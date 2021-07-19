import cv2, time
import numpy as np

img = cv2.imread('faces.jpg')

#Load a pre-trained model
face_cascade = cv2.CascadeClassifier('./model/haarcascade_frontalface_default.xml')
