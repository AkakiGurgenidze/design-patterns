from __future__ import annotations

from shapeVolumes.volume import TestConsole, get_volume, RectangularPrism, CombineShape, Sphere


def test_volume() -> None:
    console = TestConsole()

    get_volume(console)

    assert console.output == 6


def test_combine_shape() -> None:
    box_list = [RectangularPrism(side_a=2, side_b=2, side_c=2)] * 5
    boxes = CombineShape(box_list)
    book = RectangularPrism(side_a=1, side_b=1, side_c=1)
    package = CombineShape([boxes, book])

    assert package.volume() == 41


def test_sphere() -> None:
    assert CombineShape([Sphere(), RectangularPrism(1, 1, 1)]).volume() == 2
