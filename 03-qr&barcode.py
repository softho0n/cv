import cv2
import numpy as np
from pyzbar.pyzbar import decode

class Scanner:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.image = None
        assert self.cap is not None
    
    def __decoder__(self, frame):
        gray_img = cv2.cvtColor(frame, 0)
        code_info = decode(gray_img)

        for obj in code_info:
            points = obj.polygon
            (x,y,w,h) = obj.rect
            pts = np.array(points, np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(frame, [pts], True, (0, 255, 0), 3)

            barcodeData = obj.data.decode("utf-8")
            barcodeType = obj.type
            string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)
            
            cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
            print("Barcode: "+barcodeData +" | Type: "+barcodeType)

    def __call__(self):
        while True:
            ret, self.image = self.cap.read()
            if not ret:
                break

            self.__decoder__(self.image)
            cv2.imshow("QR PASS", self.image)
            key = cv2.waitKey(10)

            if key == ord("q"):
                break
            
if __name__ == "__main__" :
    scanner = Scanner()
    scanner()