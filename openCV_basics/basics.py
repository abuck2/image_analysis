import numpy as np
import cv2, time

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

###############################################
#Video
##############################################

#standard display
#videos
#args = Path
cap = cv2.VideoCapture("03_Working_on_Videos/data/clip.mp4")

#No control : 1ms is too fasr 100 frame/secons
fps = 0
while True :
    start_time = time.time()
    ret, frame = cap.read()
    if not ret:
        break
    else :
        cv2.putText(frame,'FPS: {:.0f}'.format(fps),(30,40),cv2.FONT_HERSHEY_SIMPLEX,1.5,
                (255,255,255),1)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == ord("q"):
            break
    end_time = time.time() - start_time
    fps = 1/time_taken
cap.release
cv2.destroyAllWindows()


#Correct speed, approximate
fps = 0
while True:
    start_time = time.time() # start time
    ret, frame = cap.read()
    if ret == False:
        break

    cv2.putText(frame,'FPS: {:.0f}'.format(fps),(30,40),cv2.FONT_HERSHEY_SIMPLEX,1.5,
                (255,255,255),1)
    cv2.imshow('video',frame)
    if cv2.waitKey(41) == ord('q'):
        break

    time_taken = time.time() - start_time # time taken in seconds
    fps = 1/time_taken # frames per seconds

cap.release()
cv2.destroyAllWindows()






#Giving index 0 to videocapture, should capture the camera stream
cap0 = cv2.VideoCapture(0) # 0 , 1 , ...
fps = 0
while True:
    start_time = time.time() # start time
    ret, frame0 = cap0.read()

    cv2.putText(frame0,'FPS: {:.0f}'.format(fps),(30,40),cv2.FONT_HERSHEY_SIMPLEX,1.5,
                (255,255,255),1)
    cv2.imshow('camera-1',frame0)
    if cv2.waitKey(1) == ord('q'):
        break


    time_taken = time.time() - start_time # time taken in seconds
    fps = 1/time_taken # frames per seconds

cap.release()
cv2.destroyAllWindows()

## Staacking output if more than one camera
cap0 = cv2.VideoCapture(0) # 0 , 1 , ...
cap1 = cv2.VideoCapture(1) # 0 , 1 , ...
fps = 0
while True:
    start_time = time.time() # start time
    ret, frame0 = cap0.read()
    ret, frame1 = cap1.read()

    cv2.putText(frame0,'FPS: {:.0f}'.format(fps),(30,40),cv2.FONT_HERSHEY_SIMPLEX,1.5,
                (255,255,255),1)
    cv2.putText(frame1,'FPS: {:.0f}'.format(fps),(30,40),cv2.FONT_HERSHEY_SIMPLEX,1.5,
                (255,255,255),1)

    # horizantal stack
    hstack = np.hstack((frame0,frame1))


    cv2.imshow('camera-1',frame0)
    cv2.imshow('camera-2',frame1)
    cv2.imshow('camera-12',hstack)
    if cv2.waitKey(1) == ord('q'):
        break


    time_taken = time.time() - start_time # time taken in seconds
    fps = 1/time_taken # frames per seconds

cap.release()
cv2.destroyAllWindows()

