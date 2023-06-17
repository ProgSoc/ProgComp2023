from typing import NamedTuple


class Point(NamedTuple):
    x: float
    y: float


def polygon_intersection(poly1: list[Point], poly2: list[Point]) -> list[Point]:
    # Your solution goes here
    pass


def polygon_area(points: list[Point]):
    area = 0.0
    n = len(points)

    for i in range(n):
        j = (i + 1) % n
        area += points[i].x * points[j].y
        area -= points[j].x * points[i].y

    area = abs(area) / 2.0
    return area


def read_poly():
    points = input().split()
    points = [p.split(",") for p in points]
    points = [Point(float(p[0]), float(p[1])) for p in points]
    return points


poly1 = read_poly()
poly2 = read_poly()

intersection = polygon_intersection(poly1, poly2)

print(polygon_area(intersection))
