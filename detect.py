import cv2
from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO("Models/Yolov8m  31mAp/weights/best.pt")

label = {
    0: "pedestrian",
    1: "people",
    2: "bicycle",
    3: "car",
    4: "van",
    5: "truck",
    6: "tricycle",
    7: "awning-tricycle",
    8: "bus",
    9: "motor",
}
video_path = "Media/5587732-hd_1920_1080_30fps.mp4"

#fourcc = cv2.VideoWriter_fourcc(*"XVID")
#out = cv2.VideoWriter("Media/output.avi", fourcc, 20.0, (1920, 1080))


video = cv2.VideoCapture(video_path)

while True:
    # Read a frame from the video
    ret, frame = video.read()

    # If the frame was not successfully read, exit the loop
    if not ret:
        break
    frame = cv2.resize(frame, (790, 666))

    results = model(frame, device=0)[0]
    print(results.boxes.xywh)
    for detection in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = detection
        label_name = label[class_id]
        print(x1, y1, x2, y2, score, label[class_id])
        if label_name == "car":
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(
                frame,
                label_name,
                (int(x1), int(y1)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (102, 201, 237),
                2,
            )
    #out.write(frame)
    # Display the frame
    cv2.imshow("Video", frame)

    # Wait for the 'q' key to be pressed to exit the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video file and close the window
video.release()
#out.release()
cv2.destroyAllWindows()
