import cv2 
import sys

if(len(sys.argv) != 3):
    print("Usage: python3 converter.py <inp vid> <out vid>")
    exit()

print(sys.argv[1])
print(sys.argv[2])
cap = cv2.VideoCapture(sys.argv[1])
size = (int(cap.get(3)), int(cap.get(4)))

vid_writer = cv2.VideoWriter(sys.argv[2],
                cv2.VideoWriter_fourcc(*"MJPG"), 20, size)   

while cap.isOpened():
    success, frame = cap.read()
    if success:
        gray = cv2.colorChange(frame, cv2.COLOR_BGR2GRAY)
        # vid_writer.write(gray)
        cv2.imshow("Frame", gray)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
vid_writer.release()

cv2.destroyAllWindows()