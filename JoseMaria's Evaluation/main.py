import multiprocessing
import ctypes
import numpy as np
import cv2 as cv

def load_JSON(file_path):

    import json
    with open(file_path) as obj:
        data = json.load(obj)
    return data

def initialize():

    import argparse
    parser = argparse.ArgumentParser(description='Python Synthesizer')
    parser.add_argument('--wires', help='Enter path to wires.json', default="example/wires.json")
    parser.add_argument('--mapping', help='Enter path to mapping.json', default="example/mapping.json")
    args = parser.parse_args()

    wires = load_JSON(args.wires)
    data = load_JSON(args.mapping)

    return wires, data


def shared_array(shape):
    shared_array_base = multiprocessing.Array(ctypes.c_uint8, shape[0]*shape[1])
    shared_array = np.ctypeslib.as_array(shared_array_base.get_obj())
    shared_array = shared_array.reshape(*shape)
    return shared_array

array = shared_array((480, 640))
lock = multiprocessing.Lock()

def handler(element, def_param=(lock, array)):
    
    if element == 'camera':
    
       cap = cv.VideoCapture(0)
       print("Running camera")
       
       while True:
            ret, frame = cap.read()
            frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            
            lock.acquire()
            print("lock camera")
            array[:,:] = frame[:,:]
            lock.release()
            print("unlock camera")
            
    elif element == 'screen':
    
        print("Running screen")
        img = np.array((480,640), dtype=np.uint8)
        
        while True:

            lock.acquire()
            print("lock screen acquired")
            img[:,:] = array[:,:]
            lock.release()
            print("lock screen released")
            
            cv.imshow("Screen", img)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break


if __name__ == '__main__':
        
    wires, data = initialize()    
    
    pool = multiprocessing.Pool(processes=3)

    args = []
    for i, element in enumerate(data["mapping"]):
        print(element["block_name"])
        args.append(element["block_name"])

    pool.map(handler, args)
    
    
    