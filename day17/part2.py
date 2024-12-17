import sys
from itertools import takewhile

from common import execute

registries = [
    int(line.rstrip().rpartition(" ")[2])
    for line in takewhile(lambda l: l != "\n", sys.stdin)
]

program = [int(x) for x in sys.stdin.readline().rstrip().partition(" ")[2].split(",")]


def common_suffix_len(a: list[int], b: list[int]) -> int:
    return sum(x == y for x, y in zip(reversed(a), reversed(b)))


def find_registry_a(program: list[int], registries: list[int]) -> int:
    registry_a = 0
    match_len = 0
    while (
        new_match_len := common_suffix_len(
            program,
            execute(program, [registry_a] + registries[1:]),
        )
    ) < len(program):
        if new_match_len > match_len:
            match_len = new_match_len
            registry_a <<= 3
        else:
            registry_a += 1
    return registry_a


registry_a = find_registry_a(program, registries)

assert registry_a == 164278899142333
