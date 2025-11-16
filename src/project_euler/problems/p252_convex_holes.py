from dataclasses import dataclass
from math import sqrt

import matplotlib.pyplot as plt


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

    def non_normalized_cos(self, point: Point):
        other_segment = point - self.end
        return (
            other_segment.x * self.x + other_segment.y * self.y
        ) / other_segment.length()

    def is_to_the_left(self, point: Point):
        other = point - self.start
        return other.y * self.x - other.x * self.y >= 0

    def find_closest(self, points: list[Point]):
        closest = None
        current_cos = None
        for point in points:
            if self.start == point or self.end == point:
                continue
            new_cos = self.non_normalized_cos(point)
            if closest is None or new_cos > current_cos:
                current_cos = new_cos
                closest = point
        return closest


class Polygon:
    def __init__(self, segments: list[Segment]):
        assert len(segments) >= 3, "Polygon must be made of at least three segments."
        for first, second in zip(segments, segments[1:]):
            assert first.end == second.start, (
                "The end of each segment must be the start of the next"
            )
        assert segments[0].start == segments[-1].end, (
            "The end of the last segment must be the start of the first"
        )
        self.segments = segments

    def contains(self, point):
        # only works if the polygon is convex
        return all(segment.is_to_the_left(point) for segment in self.segments)


def generate_points(
    nb_points: int,
    seed: int = 290797,
    modulus: int = 50515093,
) -> list[Point]:
    result = []
    for i in range(nb_points):
        seed = (seed * seed) % modulus
        x = (seed % 2000) - 1000
        seed = (seed * seed) % modulus
        y = (seed % 2000) - 1000
        result.append(Point(x, y))
    return result


def plot(
    points: list[Point],
    segments: list[Segment] | None = None,
):
    if segments is None:
        segments = []
    x, y = zip(*[(p.x, p.y) for p in points])
    plt.scatter(x, y)
    for segment in segments:
        plt.plot(
            [segment.start.x, segment.end.x],
            [segment.start.y, segment.end.y],
        )
    plt.show()


def find_point_with_highest_y(points: list[Point]):
    highest_point = None
    for point in points:
        if highest_point is None or point.y > highest_point.y:
            highest_point = point
    return highest_point


def main():
    points = generate_points(20)
    print(points)
    initial_point = find_point_with_highest_y(points)
    print(f"initial point: {initial_point}")
    segment = Segment.from_point_and_dir(initial_point, -1, 0)
    segments = []
    while segment.end != initial_point or not segments:
        new_segment = segment.find_closest(points) - segment.end
        segments.append(new_segment)
        segment = new_segment
    plot(points, segments)
    envelope = Polygon(segments)
    print(envelope)
    for point in points:
        assert envelope.contains(point)


def explore():
    temp = Segment(Point(x=-883, y=-38), Point(x=-893, y=-826))
    wrong_point = Point(x=-811, y=286)
    correct_point = Point(x=-454, y=-947)
    print(temp.non_normalized_cos(wrong_point))
    print(temp.non_normalized_cos(correct_point))


if __name__ == "__main__":
    main()
    # explore()
