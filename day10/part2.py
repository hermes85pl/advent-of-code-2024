import sys

from common import Point, setup

at, steps, trailheads = setup([[int(x) for x in line.rstrip()] for line in sys.stdin])


def score(pos: Point):
    stack = [pos]
    score = 0
    while stack:
        pos = stack.pop()
        stack.extend(steps(pos))
        score += at(pos) == 9
    return score


total = sum(score(pos) for pos in trailheads())

assert total == 1511
