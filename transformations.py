new_path = "04_Image_transformations"

import numpy as np
import cv2

img = cv2.imread(new_path+ '/images/flemingo.jpg')
def display(winame,img):
    cv2.imshow(winame,img)
    cv2.waitKey(2500)
    cv2.destroyAllWindows()
    
display('bird',img)

#1. Translation
# floating point matrix M = [[1, 0, Dx], [0, 1, Dy]]
#Setting the translation matrix
tx = 50 # right
ty = 90 # download
M = np.float32([[1,0,tx],
         [0,1,ty]])

#Args : image, traslation matrix, image shape
shifted_img = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
display('shifted righ 100, down 150',shifted_img)


#In a function
def translation(image,tx,ty):
    M = np.float32([[1,0,tx],
         [0,1,ty]])
    shifted_img = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
    display('shifted',shifted_img)

