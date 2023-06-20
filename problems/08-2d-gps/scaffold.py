from typing import NamedTuple


class Coordinate(NamedTuple):
    x: float
    y: float
    distance: float


def trilaterate(p1: Coordinate, p2: Coordinate, p3: Coordinate) -> tuple[float, float]:
    # Your code goes here
    return (x, y)


def read_coord():
    x, y, d = map(float, input().split())
    return Coordinate(x, y, d)


p1 = read_coord()
p2 = read_coord()
p3 = read_coord()

x, y = trilaterate(p1, p2, p3)

print(f"{int(x)} {int(y)}")
