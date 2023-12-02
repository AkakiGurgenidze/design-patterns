# https://www.codewars.com/kata/58e24788e24ddee28e000053
# LOAD REGISTER
# mov x y: copies y into register x
#   - y can be either a register or a constant.
# INCREASE REGISTER
# inc x: increases the content of the register x by one
# DECREASE REGISTER
# dec x: decreases the content of the register x by one
# JUMP
# jnz x y: jumps to an instruction y steps away, but only if x is not zero
#   - jumps relative to itself
#   - y positive means jump forward
#   - y negative means jump backward
#   - y can be either a register or a constant
#   - x can be either a register or a constant

from __future__ import annotations

from dataclasses import dataclass, field

from assembler.assembler import Assembler, Interpreter
from assembler.interpreter import Jump, Decrement, Increment, Move
from assembler.memory import Memory


@dataclass
class Tracker(Assembler):
    tracked: list[str] = field(default_factory=list)

    def execute(self, instruction) -> None:
        self.tracked.append(instruction)

    def assert_tracked(self, program: list[str]) -> None:
        assert self.tracked == program

    def create_interpreter(self) -> Interpreter:
        return self


def test_should_execute_every_instruction():
    tracker = Tracker()
    program = [f"instruction{n}" for n in range(10)]

    tracker.run(program)

    tracker.assert_tracked(program)


# Assembler(Move(Increment(Decrement(Jump()))))
def create_default_interpreter(memory):
    return Move(memory, Increment(memory, Decrement(memory, Jump(memory))))


class AAAssembler(Assembler):
    def create_interpreter(self) -> Interpreter:
        memory = Memory()
        return create_default_interpreter(memory)
