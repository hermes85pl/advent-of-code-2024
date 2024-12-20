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
    for x in range(-20, 21):
        rest = 20 - abs(x)
        for y in range(-rest, rest + 1):
            new_pos = move(pos, (x, y))
            new_steps = path.get(new_pos)
            if new_steps is not None and new_steps - steps >= 100 + abs(x) + abs(y):
                total += 1

assert total == 1020244
