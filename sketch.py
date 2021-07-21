import cv2
import numpy as np

class sketcher():
    def __init__(self, display:bool = True, blur_size:int = 5, gamma:int = 0.):
        self.blur_size = blur_size
        if gamma > 0:
            self.gamma = gamma
        else :
            self.gamma = 0.01
        

    def sketch(self, path):
        img = cv2.imread(path)
        gray = self.grayscale(img)
        blur = self.gaussian_blur(gray)
        divided = self.division_image(gray, blur)
        img = self.gamma_app(divided)
        self.display(img)


    def display(self, img):
        cv2.imshow('image',img)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()

    def grayscale(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return gray
    
    def gaussian_blur(self, img):
        blurred = cv2.GaussianBlur(img, (self.blur_size,self.blur_size), 0)
        return blurred
    
    def division_image(self, gray, blur):
        divided = cv2.divide(gray, blur, scale=256)
        return divided
    
    def gamma_app(self, img):
        inverse_gamma = 1/self.gamma
        #Lookup table
        lut = np.array([((i/255)**inverse_gamma*256) for i in range(0,256)])
        img = cv2.LUT(img.astype("uint8"), lut.astype("uint8"))
        return img
        

if __name__=="__main__":
    skt = sketcher(gamma = 0.5, blur_size = 3)
    skt.sketch("sketch.jpg")

