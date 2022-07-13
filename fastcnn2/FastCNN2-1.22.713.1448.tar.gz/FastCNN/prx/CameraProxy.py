import cv2
import time
import base64
from threading import Thread,Lock


class CV2Camera:
    def __init__(self):
        self._img = None
        self._thx = None
        self._run = False
        self._fps = 0.0
        self._width = 2592
        self._heigh = 1944
        self._lock = Lock()
        pass
    
    def startCapture(self):
        if self._thx == None:
            
            self._thx = Thread(target=self.doCapture)
            self._run = True
            self._thx.start()
            time.sleep(0.3)
        pass
    
    def stopCapture(self):
        if self._thx:
            self._run = False
            
        pass
    
    def isGrabbing(self):
        return not (self._img is None)
    
    def doCapture(self):
        cap = cv2.VideoCapture(0)
        cap.set(3,self._width)
        cap.set(4,self._heigh)
       
        while self._run:
            if cap.isOpened():
                s = time.time()
                suc,img = cap.read()
                e = time.time()
                print(e-s)
                if suc:
                    with self._lock:
                        self._img = img
                        self._fps = round(1/(e-s),2)
                else:
                    self._run = False
                #cv2.imshow("img",img)
                #cv2.imwrite("C:\\4321.jpg",img)
                #self._run = False
            else:
                self._run = False
            
                
            time.sleep(0.003)
        cap.release()
        self._img = None
        self._thx = None
        self._fps = 0.0
        #cv2.destroyAllWindows()
        pass
    
    def getCapture(self):
        rtn = {"width":self._width,"heigh":self._heigh}
        with self._lock:
            rtn["fps"] = self._fps
            rtn["stram"] = str(base64.b64encode(self._img))
            
        return rtn
        
        
    def setExposure(self,exp):
        pass


if __name__ == "__main__":
    cam = AVTCamera()
    cam.startCapture()
    
    
