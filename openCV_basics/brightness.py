import numpy as np
import cv2

path = "Project_Controlling_brightness_with_GUI_using_opencv/"
img = cv2.imread(path + 'images/car.jpg')
print(img)
def nothing(x):
    pass

cv2.namedWindow('Brightness Control')
#Args : trackbar name, windown name, default, max, a standard test function (a lambda could work)
bright = cv2.createTrackbar('Brightness','Brightness Control',75,255,nothing)
#matrix with same shape as img
value = np.ones_like(img,dtype='uint8')


while True:
    bright = cv2.getTrackbarPos('Brightness','Brightness Control')
    bar = bright - 127
    
    if bar >=0:
        value = np.ones_like(img,dtype='uint8')*bar
        img_ctrl = cv2.add(img,value)
        
    else:
        bright = 127 - bright
        value = np.ones_like(img,dtype='uint8')*bright
        img_ctrl = cv2.subtract(img,value)

        
    cv2.imshow('Brightness Control',img_ctrl)
    
    if cv2.waitKey(1) == 27: # esc button
        break
        
        
cv2.destroyAllWindows()
