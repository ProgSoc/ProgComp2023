from typing import NamedTuple


class Coordinate(NamedTuple):
    x: float
    y: float
    distance: float


def trilaterate(p1: Coordinate, p2: Coordinate, p3: Coordinate):
    # Extract the coordinates and distances from the input points
    x1, y1, r1 = p1
    x2, y2, r2 = p2
    x3, y3, r3 = p3

    # Calculate the denominators that will be used in the equations
    A = 2 * (x2 - x1)
    B = 2 * (y2 - y1)
    C = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2
    D = 2 * (x3 - x1)
    E = 2 * (y3 - y1)
    F = r1**2 - r3**2 - x1**2 + x3**2 - y1**2 + y3**2

    # Solve for x and y
    x = (C * E - F * B) / (E * A - B * D)
    y = (C * D - A * F) / (B * D - A * E)

    return (x, y)


def read_coord():
    x, y, d = map(float, input().split())
    return Coordinate(x, y, d)


p1 = read_coord()
p2 = read_coord()
p3 = read_coord()

x, y = trilaterate(p1, p2, p3)

print(f"{int(x)} {int(y)}")
