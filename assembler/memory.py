from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Memory:
    registers: dict[str, int] = field(default_factory=dict)

    def value_of(self, register: str) -> int:
        try:
            return self.registers[register]
        except KeyError:
            raise RegisterNotFound(register)

    def store(self, register: str, value: int):
        self.registers[register] = value

    def copy(self, source: str, destination: str):
        self.store(destination, self.value_of(source))

    def increment(self, register: str):
        self.registers[register] += 1

    def decrement(self, register: str):
        self.registers[register] -= 1


class RegisterNotFound(Exception):
    name: str
