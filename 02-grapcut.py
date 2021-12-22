import cv2
import argparse
import numpy as np

class GrapCut:
    def __init__(self, img_path) :
        self.img = cv2.imread(img_path)
        assert self.img is not None
        self.mask = np.zeros(self.img.shape[:2], np.uint8)
        self.bgdModel = np.zeros((1, 65), np.float64)
        self.fgdModel = np.zeros((1, 65), np.float64)
        self.dst = None
    
    def on_mouse(self, event, x, y, flags, param) :
        if event == cv2.EVENT_LBUTTONDOWN :
            cv2.circle(self.dst, (x, y), 3, (255, 0, 0), -1)
            cv2.circle(self.mask, (x, y), 3, cv2.GC_FGD, -1)
            cv2.imshow("dst", self.dst)
        elif event == cv2.EVENT_RBUTTONDOWN :
            cv2.circle(self.dst, (x, y), 3, (0, 0, 255), -1)
            cv2.circle(self.mask, (x, y), 3, cv2.GC_BGD, -1)
            cv2.imshow("dst", self.dst)
        elif event == cv2.EVENT_MOUSEMOVE :
            if flags & cv2.EVENT_FLAG_LBUTTON :
                cv2.circle(self.dst, (x, y), 3, (255, 0, 0), -1)
                cv2.circle(self.mask, (x, y), 3, cv2.GC_FGD, -1)
                cv2.imshow("dst", self.dst)
            elif flags & cv2.EVENT_FLAG_RBUTTON :
                cv2.circle(self.dst, (x, y), 3, (0, 0, 255), -1)
                cv2.circle(self.mask, (x, y), 3, cv2.GC_BGD, -1)
                cv2.imshow("dst", self.dst)

    def execute(self) :
        rc = cv2.selectROI(self.img)
        cv2.grabCut(self.img, self.mask, rc, self.bgdModel, self.fgdModel, 1, cv2.GC_INIT_WITH_RECT)

        mask2 = np.where((self.mask == 0) | (self.mask == 2), 0, 1).astype('uint8')
        self.dst = self.img * mask2[:, :, np.newaxis]

        cv2.imshow("dst", self.dst)
        cv2.setMouseCallback("dst", self.on_mouse)
        while True :
            key = cv2.waitKey()
            if key == 13 :
                cv2.grabCut(self.img, self.mask, rc, self.bgdModel, self.fgdModel, 1, cv2.GC_INIT_WITH_MASK)
                mask2 = np.where((self.mask == 0) | (self.mask == 2), 0, 1).astype('uint8')
                self.dst = self.img * mask2[:, :, np.newaxis]
                cv2.imshow("dst", self.dst)
            elif key == 27 :
                break
        cv2.destroyAllWindows()

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("--imgpath", type=str, default=None, help="image path")
    args = parser.parse_args()

    grapCut = GrapCut(args.imgpath)
    grapCut.execute()