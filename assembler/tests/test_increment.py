from __future__ import annotations

from assembler.interpreter import Increment
from assembler.memory import Memory


def test_should_increment():
    memory = Memory({"R0": 0})

    Increment(memory).execute("inc R0")

    assert memory.value_of("R0") == 1
