import cv2
import numpy as np

path = "08_Smoothing_filters/"
img = cv2.imread(path+'images/beach.jpg')

#every pixel is mixed with surrounding pixels
#1. Averaging
# Convolution kernel
# kxk sliding window, we take the average every step and assign it ti the center of the window
# K increase -> blurring increases
# What about padding and edge?
# -> answer : different paddings avalaible (0, same, ...)
blur_avg9 = cv2.blur(img,(9,9)) #9x9 window

cv2.imshow('blur 9',blur_avg9)
cv2.waitKey(5000)
cv2.destroyAllWindows()


#2. Median
#better at denoising (salt&pepper)
blur_median_3 = cv2.medianBlur(sp,3) #same but takes the median


#3. Gaussian
#Same as averaging but weighted by a gaussian
blur_gauss_7 = cv2.GaussianBlur(img,(7,7),0) #stdev x and y. 0 = auto
