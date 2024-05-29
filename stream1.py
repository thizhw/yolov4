import cv2
import time

cap = cv2.VideoCapture('http://149.202.66.6:8080/Peaky.Blinders.S06/Peaky.Blinders.S06E01.mp4')
fps = int(cap.get(cv2.CAP_PROP_FPS))
save_interval = 10

frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame_count += 1

        if frame_count % (fps * save_interval) == 0:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"frame_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Captured frame at {timestamp}")
            # optional 
            frame_count = 0

    # Break the loop
    else:
        break

cap.release()
cv2.destroyAllWindows()
