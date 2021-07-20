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


#2. Rotation
#2.1 With a rotation matrix
#M = [[a, b, (1-a)Cx-bCy],[ -b, a, bCx+(1-a)Cy]]
#Avec a = cos(t)*scale, b = sin(t)*scale
#Cx, Cy coordinates of the center
center = (img.shape[1]//2,img.shape[0]//2) #integer part of half
M = cv2.getRotationMatrix2D(center,45,1) #center, angle, scale
rotate_45 = cv2.warpAffine(img,M,(img.shape[1],img.shape[0])) #Rotation
display('rotate 45 anti clock',rotate_45)

#in a funtion
def rotate(image,angle,scale):
    center = (image.shape[1]//2,image.shape[0]//2)
    M = cv2.getRotationMatrix2D(center,angle,scale)
    rotate_img = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))

    display('rotate',rotate_img)


#3. resize
img_resize = cv2.resize(img,(300,300),interpolation=cv2.INTER_AREA) 
#check the interpolations techniques inter_cubic is better for large images but slow 

#4. flipping
flip_img = cv2.flip(img,0) # 1 = h,-1 = v,0 = both

#5. cropping
crop = img[100:400,100:400]



