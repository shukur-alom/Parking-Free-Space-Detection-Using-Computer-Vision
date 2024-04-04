import pickle
from shapely.geometry import Polygon


def find_polygon_center(points):
    """Find the center of a polygon given its points."""
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    center_x = int(sum(x_coords) / len(points))
    center_y = int(sum(y_coords) / len(points))
    return (center_x, center_y)


def save_object(poligon):
    """Save the polygon object to a file."""
    with open("object/poligon.obj", "wb") as f:
        pickle.dump(poligon, f)


def load_object():
    """Load the polygon object from a file."""
    try:
        with open("object/poligon.obj", "rb") as f:
            return pickle.load(f)
    except:
        save_object([])

        with open("object/poligon.obj", "rb") as f:
            return pickle.load(f)


def IoU(polygon_1, polygon_2):
    """Calculate the Intersection over Union (IoU) of two polygons."""
    polygon_1 = Polygon(polygon_1)
    polygon_2 = Polygon(polygon_2)
    intersect = polygon_1.intersection(polygon_2).area
    union = polygon_1.union(polygon_2).area
    iou = intersect / union
    return iou


def is_point_in_polygon(point, polygon):
    """Check if a point is inside a polygon."""
    x, y = point
    poly_points = [(x, y) for x, y in polygon]
    n = len(poly_points)
    inside = False

    p1x, p1y = poly_points[0]
    for i in range(n + 1):
        p2x, p2y = poly_points[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside


def box_center(x1, y1, x2, y2):
    """Find the center of a bounding box."""
    center_x = int((x1 + x2) / 2)
    center_y = int((y1 + y2) / 2)
    return (center_x, center_y)


def get_label_name(n):
    """Return the label names."""
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
    return label[n]
