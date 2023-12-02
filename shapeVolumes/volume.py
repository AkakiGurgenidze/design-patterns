from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol


class Console(Protocol):
    def read_int(self) -> int:
        pass

    def print_int(self, value: int) -> None:
        pass


@dataclass
class TestConsole:
    output: int = 0
    count: int = 0

    def read_int(self) -> int:
        self.count += 1
        return self.count

    def print_int(self, volume: int) -> None:
        self.output = volume


class RealConsole:
    def read_int(self) -> int:
        return int(input())

    def print_int(self, value: int) -> None:
        print(value)


def get_volume(console: Console) -> None:
    prism = RectangularPrism(
        side_a=console.read_int(),
        side_b=console.read_int(),
        side_c=console.read_int(),
    )

    console.print_int(prism.volume())


@dataclass
class RectangularPrism:
    side_a: int
    side_b: int
    side_c: int

    def volume(self) -> int:
        return self.side_a * self.side_b * self.side_c


@dataclass
class Sphere:
    def volume(self) -> int:
        return 1


class Shape(Protocol):
    def volume(self) -> int:
        pass


@dataclass
class CombineShape:
    shapes: list[Shape]

    def volume(self) -> int:
        return sum(shape.volume() for shape in self.shapes)
