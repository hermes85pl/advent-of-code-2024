import sys
from itertools import takewhile

A = 0
B = 1
C = 2


def load():
    registries = [
        int(line.rstrip().rpartition(" ")[2])
        for line in takewhile(lambda l: l != "\n", sys.stdin)
    ]
    program = [
        int(x) for x in sys.stdin.readline().rstrip().partition(" ")[2].split(",")
    ]
    return registries, program


def combo_operand(operand: int, registries: list[int]) -> int:
    return operand if operand < 4 else registries[operand % 4]


def execute(program: list[int], registries: list[int]) -> list[int]:
    opcode_idx = 0
    output: list[int] = []

    while opcode_idx < len(program):
        opcode = program[opcode_idx]
        operand = program[opcode_idx + 1]
        opcode_idx += 2

        if opcode == 0:
            registries[A] //= 2 ** combo_operand(operand, registries)
        elif opcode == 1:
            registries[B] ^= operand
        elif opcode == 2:
            registries[B] = combo_operand(operand, registries) % 8
        elif opcode == 3:
            if registries[A] != 0:
                opcode_idx = operand
        elif opcode == 4:
            registries[B] ^= registries[C]
        elif opcode == 5:
            output.append(combo_operand(operand, registries) % 8)
        elif opcode == 6:
            registries[B] = registries[A] // 2 ** combo_operand(operand, registries)
        elif opcode == 7:
            registries[C] = registries[A] // 2 ** combo_operand(operand, registries)

    return output
