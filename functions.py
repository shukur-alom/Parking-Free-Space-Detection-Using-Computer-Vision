def find_polygon_center(points):
    '''Find the center of a polygon given its points.'''
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    center_x = int(sum(x_coords) / len(points))
    center_y = int(sum(y_coords) / len(points))
    return (center_x, center_y)
