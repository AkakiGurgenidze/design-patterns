from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from assembler.interpreter import Jump, UnknownInstructionError
from assembler.memory import Memory
from assembler.program import Program


def test_should_not_jump():
    program = MagicMock(spec=Program)

    Jump(program=program).execute("jnz 0 1")

    program.jump.assert_not_called()


def test_should_jump_by_one():
    program = MagicMock(spec=Program)

    Jump(program=program).execute("jnz 1 1")

    program.jump.assert_called_once_with(1)


def test_should_jump_based_on_register_condition():
    program = MagicMock(spec=Program)

    Jump(Memory({"R0": 0}), program).execute("jnz R0 2")

    program.jump.assert_not_called()


def test_should_jump_by_steps_in_register():
    program = MagicMock(spec=Program)

    Jump(Memory({"R0": 2}), program).execute("jnz 1 R0")

    program.jump.assert_called_once_with(2)


def test_should_fail_on_unknown_instruction():
    with pytest.raises(UnknownInstructionError):
        Jump().execute("unknown")
