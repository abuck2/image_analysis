import numpy as np
import cv2
path = "Project_FaceDetection_with_DNN_opencv"
models_path = "Project_FaceDetection_with_DNN_opencv/models/"

img = cv2.imread(path + '/faces.jpg')

cv2.imshow('face',img)
cv2.waitKey(2000)
cv2.destroyAllWindows()

face_detection_model = cv2.dnn.readNetFromCaffe(models_path+'deploy.prototxt.txt',
                                                models_path+'res10_300x300_ssd_iter_140000_fp16.caffemodel')

def face_detection_dnn(img):
    # args, img, image, size, rgd, bgrToRgd
    blob = cv2.dnn.blobFromImage(img,1,(300,300),(104,177,123),swapRB=True)
    # Set blob as input
    face_detection_model.setInput(blob)
    # Prediction : 4 dimesional array, 200 faces, third value is the confidence score, second is binary class, then boundaries
    detections = face_detection_model.forward()
    #detections[0,0,:,2] -> print all probas
    #  Drawing rectangles from detection
    image = img.copy()
    h,w = image.shape[:2]
    for i in range(0,detections.shape[2]):
        confidence = detections[0,0,i,2]
        if confidence > 0.5:
            # diagonal points 3: 7
            box = detections[0,0,i,3:7]*np.array([w,h,w,h]) #boxes are normalized to image size
            box = box.astype('int')
            pt1 = (box[0],box[1])
            pt2 = (box[2],box[3])
            # draw rectangle
            cv2.rectangle(image,pt1,pt2,(0,255,0),1)

            text = 'score : {:.0f} %'.format(confidence*100)
            cv2.putText(image,text,pt1,cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

    return image

img_detect = face_detection_dnn(img)
cv2.imshow('face detection',img_detect)
cv2.waitKey(2500)
cv2.destroyAllWindows()

#From a stream
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret == False:
        break

    img_detection = face_detection_dnn(frame)

    cv2.imshow('Real Time Face Detection with DNN',img_detection)
    if cv2.waitKey(1) == ord('a'):
        break

cap.release()
cv2.destroyAllWindows()
