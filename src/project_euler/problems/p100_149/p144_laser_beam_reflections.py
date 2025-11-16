from dataclasses import dataclass
from math import sqrt


@dataclass
class Point:
    x: int
    y: int

    def __sub__(self, other) -> Segment:
        return Segment(other, self)


class Segment:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

        self.x = self.end.x - self.start.x
        self.y = self.end.y - self.start.y

    @classmethod
    def from_point_and_dir(cls, point, x, y):
        return cls(Point(point.x - x, point.y - y), point)

    def __repr__(self):
        return f"Segment({self.start}, {self.end})"

    def length(self):
        return sqrt(self.x**2 + self.y**2)

    def reflect(self) -> Segment:
        pass