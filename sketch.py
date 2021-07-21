import cv2
import numpy as np

class sketcher():
    def __init__(self, display:bool = True):
        pass

    def sketch(self, path):
        img = cv2.imread(path)
        img = self.grayscale(img)

    def display(self, img):
        cv2.imshow('image',img)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()

    def grayscale(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        

if __name__=="__main__":
    skt = sketcher()
    skt.sketch("sketch.jpg")
