from __future__ import annotations

from dataclasses import dataclass, field

from assembler.assembler import Interpreter
from assembler.memory import Memory, RegisterNotFound
from assembler.program import Program


class Fail:
    def execute(self, instruction: str):
        raise UnknownInstructionError(instruction)


@dataclass
class UnknownInstructionError(Exception):
    instruction: str


@dataclass
class Move:
    memory: Memory

    following: Interpreter = field(default_factory=Fail)

    def execute(self, instruction: str) -> None:
        if not instruction.startswith("move"):
            return self.following.execute(instruction)

        _, destination, source = instruction.split()

        try:
            self.memory.copy(source, destination)
        except RegisterNotFound:
            self.memory.store(destination, int(source))


@dataclass
class Increment:
    memory: Memory

    following: Interpreter = field(default_factory=Fail)

    def execute(self, instruction: str) -> None:
        if not instruction.startswith("inc"):
            return self.following.execute(instruction)

        _, register = instruction.split()

        self.memory.increment(register)


@dataclass
class Decrement:
    memory: Memory

    following: Interpreter = field(default_factory=Fail)

    def execute(self, instruction: str) -> None:
        if not instruction.startswith("dec"):
            return self.following.execute(instruction)

        _, register = instruction.split()
        self.memory.decrement(register)


@dataclass
class Jump:
    memory: Memory = field(default_factory=Memory)
    program: Program = field(default_factory=Program)
    following: Interpreter = field(default_factory=Fail)

    def execute(self, instruction: str) -> None:
        if not instruction.startswith("jnz"):
            return self.following.execute(instruction)

        _, condition, step = instruction.split()

        if self._value_of(condition) != 0:
            self.program.jump(self._value_of(step))

    def _value_of(self, register_or_constant: str) -> int:
        try:
            return int(register_or_constant)
        except ValueError:
            return self.memory.value_of(register_or_constant)
