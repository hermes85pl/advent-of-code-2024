import sys

from common import setup

at, steps, trailheads = setup([[int(x) for x in line.rstrip()] for line in sys.stdin])


def score(pos: tuple[int, int]):
    visited = set()
    queue = [pos]
    score = 0
    while queue:
        pos = queue.pop(0)
        if pos not in visited:
            visited.add(pos)
            queue.extend(steps(pos))
            score += at(pos) == 9
    return score


total = sum(score(pos) for pos in trailheads())

assert total == 682
