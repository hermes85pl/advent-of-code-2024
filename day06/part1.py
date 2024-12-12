import sys

from common import move, setup, turn

at, pos, dir = setup([line.rstrip() for line in sys.stdin])

places = {pos}

while True:
    new_pos = move(pos, dir)
    new_val = at(new_pos)
    if not new_val:
        break
    if new_val == "#":
        dir = turn(dir)
    else:
        pos = new_pos
        places.add(pos)

total = len(places)

assert total == 4964
