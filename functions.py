import pickle


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
        with open("object/poligon.obj", "wb") as f:
            pickle.dump([], f)
