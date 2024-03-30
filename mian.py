import cv2

cap = cv2.VideoCapture("Media/3214448-hd_1920_1080_25fps.mp4")

if cap.isOpened() == False:
    print("Error opening video file")


while cap.isOpened():


    ret, frame = cap.read()
    if ret == True:

        cv2.imshow("Frame", frame)


        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    else:
        break


cap.release()

# Closes all the frames
cv2.destroyAllWindows()
