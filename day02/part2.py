import sys

from common import safe


def anysafe(levels: list[int]) -> bool:
    return any(safe(levels[:i] + levels[i + 1 :]) for i in range(len(levels)))


total = sum(anysafe([int(x) for x in line.split()]) for line in sys.stdin)

assert total == 493
