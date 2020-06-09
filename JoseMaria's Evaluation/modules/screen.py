import cv2 as cv

def screen(sh_mem, lock):

    while(True):
    
        lock.acquire()
        img = sh_mem[:,:]
        lock.release()

        if img is not None:
            cv.imshow("Screen", img)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
