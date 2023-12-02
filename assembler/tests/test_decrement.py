from __future__ import annotations

from assembler.interpreter import Decrement
from assembler.memory import Memory


def test_should_decrement():
    memory = Memory({"R0": 1})

    Decrement(memory).execute("dec R0")

    assert memory.value_of("R0") == 0
