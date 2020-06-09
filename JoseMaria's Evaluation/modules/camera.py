import cv2 as cv

def camera(sh_mem, lock):

   cap = cv.VideoCapture(0)

   while(True):
        ret, frame = cap.read()
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame[:,:] = 255
        
        lock.acquire()
        sh_mem = frame[:,:]
        lock.release()
