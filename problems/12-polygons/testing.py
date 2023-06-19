from typing import NamedTuple
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle


class Point(NamedTuple):
    x: float
    y: float


def plot_polygons(polygons):
    fig, ax = plt.subplots()

    for poly_points, color in polygons:
        polygon = Polygon(poly_points, closed=True, fill=False, color=color)
        ax.add_patch(polygon)

    ax.set_aspect("equal", "box")
    plt.autoscale()
    plt.show()


def segment_intersection(segment1: tuple[Point, Point], segment2: tuple[Point, Point]):
    xdiff = (segment1[0].x - segment1[1].x, segment2[0].x - segment2[1].x)
    ydiff = (segment1[0].y - segment1[1].y, segment2[0].y - segment2[1].y)

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return None  # Lines don't intersect

    d = (det(*segment1), det(*segment2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div

    # Check if the intersection is within the segments
    if (
        min(segment1[0].x, segment1[1].x) <= x <= max(segment1[0].x, segment1[1].x)
        and min(segment1[0].y, segment1[1].y) <= y <= max(segment1[0].y, segment1[1].y)
        and min(segment2[0].x, segment2[1].x) <= x <= max(segment2[0].x, segment2[1].x)
        and min(segment2[0].y, segment2[1].y) <= y <= max(segment2[0].y, segment2[1].y)
    ):
        return Point(x, y)
    return None


def cross_product(A: Point, B: Point, C: Point) -> float:
    AB = Point(B.x - A.x, B.y - A.y)
    AC = Point(C.x - A.x, C.y - A.y)
    return AB.x * AC.y - AB.y * AC.x


def is_exiting(A: Point, B: Point, C: Point) -> bool:
    return cross_product(A, B, C) < 0


class Intersection(NamedTuple):
    point: Point
    index1: int
    index2: int
    entering: bool = False


def polygon_intersection(poly1: list[Point], poly2: list[Point]):
    # Compute all intersections between edges

    intersections: list[Intersection] = []
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            intersection = segment_intersection(
                (poly1[i - 1], poly1[i]), (poly2[j - 1], poly2[j])
            )
            if intersection is not None:
                exiting = is_exiting(poly1[i - 1], poly1[i], poly2[j])
                intersections.append(Intersection(intersection, i, j, not exiting))

    entering_intersection = [
        intersection for intersection in intersections if intersection.entering
    ][0]

    exiting_intersection = [
        intersection for intersection in intersections if not intersection.entering
    ][0]

    def get_poly_segment(poly: list[Point], start: int, end: int):
        if end <= start:
            return poly[start:] + poly[:end]
        return poly[start:end]

    seg1 = get_poly_segment(
        poly1, exiting_intersection.index1, entering_intersection.index1
    )
    seg2 = get_poly_segment(
        poly2, entering_intersection.index2, exiting_intersection.index2
    )

    new_poly = (
        [entering_intersection.point] + seg2 + [exiting_intersection.point] + seg1
    )

    print(seg1)
    print(seg2)
    print(new_poly)

    fig, ax = plt.subplots()

    # polygon = Polygon(poly1, closed=True, fill=False, color="red")
    # ax.add_patch(polygon)

    # polygon = Polygon(poly2, closed=True, fill=False, color="blue")
    # ax.add_patch(polygon)

    polygon = Polygon(new_poly, closed=True, fill=False, color="green")
    ax.add_patch(polygon)

    ax.set_aspect("equal", "box")
    plt.autoscale()
    plt.show()

    return new_poly


def polygon_area(points: list[Point]):
    area = 0.0
    n = len(points)

    for i in range(n):
        j = (i + 1) % n
        area += points[i].x * points[j].y
        area -= points[j].x * points[i].y

    area = abs(area) / 2.0
    return area


poly1 = [Point(0, 0), Point(0, 10), Point(10, 10), Point(10, 0)]
poly2 = [Point(5, 5), Point(5, 15), Point(15, 15), Point(15, 5)]

# poly1 = [Point(0, 0), Point(0, 10), Point(10, 10), Point(10, 0)]
# poly2 = [Point(15, 3), Point(5, 5), Point(15, 7)]

# poly1 = [Point(0, 0), Point(0, 10), Point(10, 10), Point(10, 0)]
# poly2 = [Point(2, 5), Point(5, 7), Point(15, 5), Point(5, 3)]

# poly2 = [Point(0, 0), Point(0, 10), Point(10, 10), Point(10, 0)]
# poly1 = [Point(2, 5), Point(5, 7), Point(15, 5), Point(5, 3)]

intersection = polygon_intersection(poly1, poly2)
print(polygon_area(intersection))

# plot_polygons([(poly1, "red"), (poly2, "blue")])
