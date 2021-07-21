import cv2
import numpy as np

rectangle = np.zeros((300,300),dtype='uint8')
cv2.rectangle(rectangle,(25,25),(275,275),255,-1)

circle = np.zeros((300,300),dtype='uint8')
cv2.circle(circle,(150,150),150,255,-1)

#1. AND
img_and = cv2.bitwise_and(rectangle,circle)

#2. OR
img_or = cv2.bitwise_or(rectangle,circle)

#3. NOT
img_not = cv2.bitwise_not(rectangle)

#4. XOR
img_xor = cv2.bitwise_xor(rectangle,circle)

