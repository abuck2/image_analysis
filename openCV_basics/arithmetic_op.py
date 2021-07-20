import numpy as np
import cv2

path = path = "05_Arithmetic_Operations/"
img = cv2.imread(paht + 'images/car.jpg')


#Value must stay between 0 and 255
#Addition
value = np.ones_like(img,dtype='uint8')*50
img_add = cv2.add(img,value)

#Soustraction
value = np.ones_like(img,dtype='uint8')*75
img_sub = cv2.subtract(img,value)


#Blending
img1 = cv2.imread(path + 'images/blend_1.jpg')
img2 = cv2.imread(path + 'images/blend_2.jpg')
#Args = img1, weight1, img2, weight2, add
blend = cv2.addWeighted(img1,0.5,img2,0.5,40)


