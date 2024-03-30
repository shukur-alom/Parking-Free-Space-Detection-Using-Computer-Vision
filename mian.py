import cv2
import numpy as np

# List to store points
points = []
poligon = []


def find_polygon_center(points):
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    center_x = int(sum(x_coords) / len(points))
    center_y = int(sum(y_coords) / len(points))
    return (center_x, center_y)


# Function to draw polygon
def draw_polygon(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        points.append((x, y))


# Create a black image, a window and bind the function to window
cap = cv2.VideoCapture("Media/3214448-hd_1920_1080_25fps.mp4")
cv2.namedWindow("image")
cv2.setMouseCallback("image", draw_polygon)

while 1:
    ret, frame = cap.read()
    if not ret:
        break
    mask = np.zeros_like(frame)
    for cou, i in enumerate(poligon):
        center_x, center_y = find_polygon_center(i)
        frame = cv2.putText(
            frame,
            f"s{cou}",
            (center_x, center_y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (110, 201, 250),
            1,
            cv2.LINE_AA,
        )
        cv2.fillPoly(mask, [np.array(i)], (124, 255, 112))

    frame = cv2.addWeighted(mask, 0.2, frame, 1, 0)

    for x, y in points:
        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

    cv2.imshow("image", frame)

    wail_key = cv2.waitKey(1)

    if wail_key == ord("s"):
        if len(points) > 0:
            poligon.append(points)
            points = []

    elif wail_key == ord("r"):
        try:
            poligon.pop()
        except:
            pass
    elif wail_key & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
