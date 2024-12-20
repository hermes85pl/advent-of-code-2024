import sys

from common import DIRS, setup

findpath, locate, move = setup([line.rstrip() for line in sys.stdin])

start = locate("S")
end = locate("E")

path = findpath(start, end)
assert path is not None

steps_without_cheating = len(path) - 1
assert steps_without_cheating == 9484

total = 0

for pos, steps in path.items():
    for x, y in DIRS:
        new_pos = move(pos, (2 * x, 2 * y))
        new_steps = path.get(new_pos)
        if new_steps is not None and new_steps - steps >= 100 + 2:
            total += 1

assert total == 1402
