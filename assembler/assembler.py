from __future__ import annotations

from abc import abstractmethod, ABC
from typing import Protocol, Iterable


class Assembler(ABC):
    # interpreter: Interpreter

    def run(self, program: Iterable[str]) -> None:
        interpreter = self.create_interpreter()
        for instruction in program:
            interpreter.execute(instruction)

    @abstractmethod
    def create_interpreter(self) -> Interpreter:
        pass


class Interpreter(Protocol):
    def execute(self, instruction: str):
        pass
