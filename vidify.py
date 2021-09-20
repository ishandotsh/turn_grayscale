import cv2
import numpy as np
import glob

def to_vid(directory, vid_out):
    if directory[-1] != '/':
        directory = directory + '/'
    
    img_array = []
    for filename in glob.glob(f'{directory}*.jpg'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
    
    
    out = cv2.VideoWriter(vid_out,
            cv2.VideoWriter_fourcc(*'MJPG'), 15, size)
    
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

to_vid("frames", "vg.avi")