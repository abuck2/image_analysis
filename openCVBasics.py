import numpy as np
import cv2

img = cv2.imread("01_Image_Basics/images/flemingo.jpg")

#BGR format in openCV :
print(img.shape)
#print(img)

cv2.imwrite("01_Image_Basics/images/flemingo_copy.jpg", img)

b,g,r = cv2.split(img)
cv2.imshow('color',img)
cv2.imshow('blue',b)
cv2.imshow('red',r)
cv2.imshow('green',g)
cv2.waitKey(0)
cv2.destroyAllWindows()

#conversion
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# change first 100 rows and 100 columns to green color
green = (0,255,0)
img[0:100,0:100] = green

canvas = np.zeros((300,300,3),dtype = "uint8")

def display(name:str, img):
    #Display image
    cv2.imshow(name, img)
    cv2.waitKey(2500)
    cv2.destroyAllWindows()

green = (0,255,0)

#Arguments : image, start point, end point, colour,pixel thickness
cv2.line(canvas, (0,0), (300,300), green, 3)
display("canvas", canvas)

cv2.rectangle(canvas, (10,10), (150, 300), green, 2)
display("canvas", canvas)

#thickness -1 = fill the image
cv2.rectangle(canvas, (10,10), (150, 300), green, -1)
display("canvas", canvas)

centerx, centery = canvas.shape[1]//2, canvas.shape[0]//2

white = (255,255,255)

for r in range(0,175,25):
    cv2.circle(canvas, (centerx, centery), r, white)

display("canvas", canvas)
