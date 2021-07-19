import cv2, time
import numpy as np

img = cv2.imread('faces.jpg')

#Load a pre-trained model
face_cascade = cv2.CascadeClassifier('model.xml')

#Load the image in grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Applay grayscale to cascade class : object, #of detection
boxes, detections = face_cascade.detectMultiScale2(gray)


print(boxes) #4 lignes = 4 visages, x, Y, height, width
print(detections)  # We need to find a threshold of minN (6 for ex)

def detection(img):
    boxes, detections = face_cascade.detectMultiScale2(gray, minNeighbors=6)

    #Drawing boxes
    image = img.copy()
    for x, y, w, h in boxes:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255,0,0), 1)
    cv2.imshow("boxes", image)
    cv2.waitKey(2500)
    cv2.destroyAllWindows()
    return image
