import cv2
import numpy as np

class GUIsketcher():
    def __init__(self,path:str):
        
        self.blur_size = 0
        self.gamma = 0
        
        
        self.img = cv2.imread(path)
        
    def GUI_sketch(self):
        cv2.namedWindow("Control panel")
        cv2.createTrackbar("ksize", "Control panel", 1, 100, (lambda x:None))
        cv2.createTrackbar("gamma", "Control panel", 1, 100, (lambda x:None))
        while True:
            #ksize
            k = cv2.getTrackbarPos("ksize", "Control panel")
            blur = 2*k+1
            
            g = cv2.getTrackbarPos("gamma", "Control panel")
            gamma = g/100
            
            self._sketch(gamma, blur)

            if cv2.waitKey(1) == 27:
                break


    def _sketch(self, gamma:float, blur:int):  
        img = self.img
        gray = self._grayscale(img)
        blur = self._gaussian_blur(gray, blur)
        divided = self._division_image(gray, blur)
        img = self._gamma_app(divided, gamma)
        self.display(img)


    def display(self, img):
        cv2.imshow('image',img)
        cv2.waitKey(10000)
        cv2.destroyAllWindows()

    def _grayscale(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return gray
    
    def _gaussian_blur(self, img, blur:int):
        blurred = cv2.GaussianBlur(img, (blur, blur), 0)
        return blurred
    
    def _division_image(self, gray, blur):
        divided = cv2.divide(gray, blur, scale=256)
        return divided
    
    def _gamma_app(self, img, gamma:float):
        if gamma > 0 and gamma < 1:
            inverse_gamma = 1/gamma
        else : 
            raise ValueError("Gamma value must be between 0 and 1")
        #Lookup table
        lut = np.array([((i/255)**inverse_gamma*256) for i in range(0,256)])
        img = cv2.LUT(img.astype("uint8"), lut.astype("uint8"))
        return img
        

if __name__=="__main__":
    skt = GUIsketcher("sketch.jpg")
    skt.GUI_sketch()

