import random
from dataclasses import dataclass
from typing import Protocol, Iterator, Generator

from typing_extensions import Self


@dataclass
class Creature:
    speed: int
    stamina: int
    power: int
    health: int

    def distance_until_exhausted(self) -> int:
        return self.speed * self.stamina


@dataclass
class CreatureBuilder:
    speed: int = 0
    stamina: int = 0
    power: int = 0
    health: int = 0

    def and_speed(self, value: int) -> Self:
        return self.with_speed(value)

    def with_speed(self, value: int) -> Self:
        self.speed = value

        return self

    def and_stamina(self, value: int) -> Self:
        return self.with_stamina(value)

    def with_stamina(self, value: int) -> Self:
        self.stamina = value

        return self

    def and_power(self, value: int) -> Self:
        return self.with_power(value)

    def with_power(self, value: int) -> Self:
        self.power = value

        return self

    def and_health(self, value: int) -> Self:
        return self.with_health(value)

    def with_health(self, value: int) -> Self:
        self.health = value

        return self

    def build(self) -> Creature:
        return Creature(
            speed=self.speed,
            stamina=self.stamina,
            power=self.power,
            health=self.health,
        )


class AttributeGenerator(Protocol):
    def get_speed(self) -> int:
        pass

    def get_stamina(self) -> int:
        pass

    def get_power(self) -> int:
        pass

    def get_health(self) -> int:
        pass


def random_integer_sequence() -> Generator[int, None, None]:
    yield random.randint(0, 100)


@dataclass
class GeneratorFromSequence:
    sequence: Iterator[int]

    def integer(self) -> int:
        return next(self.sequence)

    def get_speed(self) -> int:
        return self.integer()

    def get_stamina(self) -> int:
        return self.integer()

    def get_power(self) -> int:
        return self.integer()

    def get_health(self) -> int:
        return self.integer()


@dataclass
class RandomAttributeGenerator:
    def get_speed(self) -> int:
        return random.randint(0, 10)

    def get_stamina(self) -> int:
        return random.randint(0, 1000)

    def get_power(self) -> int:
        return random.randint(0, 20)

    def get_health(self) -> int:
        return random.randint(0, 1000)


@dataclass
class Evolution:
    builder: CreatureBuilder
    random: AttributeGenerator

    def evolve(self) -> None:
        (
            self.builder.with_speed(self.random.get_speed())
            .with_stamina(self.random.get_stamina())
            .with_power(self.random.get_power())
            .with_health(self.random.get_health())
        )
