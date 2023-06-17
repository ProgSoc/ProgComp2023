from typing import NamedTuple
import random


class PerfectTriangle(NamedTuple):
    x: float
    y: float
    distance: float

    def get_mult(self, mult: float):
        return PerfectTriangle(self.x * mult, self.y * mult, self.distance * mult)

    def flip_x(self):
        return PerfectTriangle(-self.x, self.y, self.distance)

    def flip_y(self):
        return PerfectTriangle(self.x, -self.y, self.distance)

    def flip_axes(self):
        return PerfectTriangle(self.y, self.x, self.distance)

    def get_random_flip(self):
        x = self
        if random.random() < 0.5:
            x = x.flip_x()
        if random.random() < 0.5:
            x = x.flip_y()
        if random.random() < 0.5:
            x = x.flip_axes()
        return x

    def get_random_mult(self):
        max_dist = 10000
        max_mult = max_dist / self.distance
        mult = int(max(random.random() * max_mult, 1))
        return self.get_mult(mult)

    def get_random(self):
        return self.get_random_mult().get_random_flip()

    def offset(self, x, y):
        return PerfectTriangle(self.x + x, self.y + y, self.distance)


perfect_tris = [
    PerfectTriangle(3, 4, 5),
    PerfectTriangle(12, 5, 13),
    PerfectTriangle(8, 15, 17),
    PerfectTriangle(7, 24, 25),
]

rand_x = int(random.random() * 10000)
rand_y = int(random.random() * 10000)


def print_tri(tri: PerfectTriangle):
    print(f"{tri.x} {tri.y} {tri.distance}")


def random_tri():
    return (
        perfect_tris[int(random.random() * len(perfect_tris))]
        .get_random()
        .offset(rand_x, rand_y)
    )


print_tri(random_tri())
print_tri(random_tri())
print_tri(random_tri())
