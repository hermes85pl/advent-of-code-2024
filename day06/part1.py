import sys

from common import move, setup, turn

fits, pos, dir = setup([line.rstrip() for line in sys.stdin])

places = {pos}

while True:
    new_pos = move(pos, dir)
    new_fit = fits(new_pos)
    if not new_fit:
        break
    if new_fit == "#":
        dir = turn(dir)
    else:
        pos = new_pos
        places.add(pos)

total = len(places)

assert total == 4964
