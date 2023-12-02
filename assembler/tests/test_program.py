from __future__ import annotations

from assembler.program import Program


def test_should_not_increment_after_jump():
    program = Program([f"instruction{n}" for n in range(3)])

    executed = []
    for instruction in program:
        program.jump(2)
        executed.append(instruction)

    assert executed == ["instruction0", "instruction2"]
