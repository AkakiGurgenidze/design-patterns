from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterator


@dataclass
class ProgramCounter:
    value: int = 0

    def pick(self, instructions: list[str]) -> str:
        self.value += 1

        return instructions[self.value - 1]

    def increment(self) -> None:
        self.value += 1

    def jump(self, value: int) -> None:
        self.value += value - 1

    def reset(self) -> None:
        self.value = 0


@dataclass
class Program:
    instructions: list[str] = field(default_factory=list)
    pc: ProgramCounter = field(default_factory=ProgramCounter)

    def jump(self, value: int) -> None:
        self.pc.jump(value)

    def __iter__(self) -> Iterator[str]:
        self.pc.reset()

        return self

    def __next__(self) -> str:
        try:
            return self.pc.pick(self.instructions)
        except IndexError:
            raise StopIteration
