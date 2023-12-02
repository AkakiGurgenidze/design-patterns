from __future__ import annotations

from assembler.interpreter import Move
from assembler.memory import Memory


def test_should_store() -> None:
    memory = Memory()

    Move(memory).execute("move R0 0")

    assert memory.value_of("R0") == 0


def test_should_copy() -> None:
    memory = Memory({"R0": 0})

    Move(memory).execute("move R1 R0")

    assert memory.value_of("R1") == 0


def test_should_overwrite() -> None:
    memory = Memory({"R0": 0, "R1": 1})

    Move(memory).execute("move R1 R0")

    assert memory.value_of("R1") == 0
