import cv2
import os

def to_frames(vid_source, directory):
    os.mkdir(directory)
    f_num = 0
    source = cv2.VideoCapture(vid_source)
    while True:
        ret, img = source.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cv2.imshow("Live", gray)
        fname = '0'*(8-len(str(f_num))) + str(f_num)
        cv2.imwrite(f'{directory}/f{fname}.jpg', gray)
        f_num += 1

        key = cv2.waitKey(1)
        if key == ord("q"):
            break
      
    cv2.destroyAllWindows()
    source.release()

