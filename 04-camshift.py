import cv2
import numpy as np
import argparse

class CamShift:
    def __init__(self, videoPath=None):
        self.cap1 = cv2.VideoCapture(videoPath)
        self.cap2 = cv2.VideoCapture(videoPath)
        assert self.cap1 is not None
        assert self.cap2 is not None

        self.x, self.y, self.w, self.h = None, None, None, None
        self.rc = None

        self.roi, self.roi_hsv, self.hist = None, None, None
        self.channels = [0, 1]
        self.ranges = [0, 180, 0, 256]

        self.term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

    def selectROI(self):
        ret, firstFrame = self.cap2.read()
        assert firstFrame is not None

        if not ret:
            exit(1)

        self.rc = cv2.selectROI(firstFrame)
        self.x = list(self.rc)[0]
        self.y = list(self.rc)[1]
        self.w = list(self.rc)[2]
        self.h = list(self.rc)[3]
        
        self.roi = firstFrame[self.y:self.y+self.h, self.x:self.x+self.w]
        self.roi_hsv = cv2.cvtColor(self.roi, cv2.COLOR_BGR2HSV)
        self.hist = cv2.calcHist([self.roi_hsv], self.channels, None, [90, 128], self.ranges)
    
    def execute(self):
        self.selectROI()

        while True:
            ret, frame = self.cap1.read()
            
            if not ret:
                break

            frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            backproj = cv2.calcBackProject([frame_hsv], self.channels, self.hist, self.ranges, 1)

            ret, self.rc = cv2.CamShift(backproj, self.rc, self.term_crit)

            cv2.rectangle(frame, self.rc, (0, 0, 255), 2)
            cv2.ellipse(frame, ret, (0, 255, 0), 2)
            cv2.imshow('frame', frame)

            if cv2.waitKey(60) == 27:
                break
        
        self.cap1.release()
        self.cap2.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--videopath", type=str, default=None, help="set video path")
    args = parser.parse_args()

    cs = CamShift(args.videopath)
    cs.execute()