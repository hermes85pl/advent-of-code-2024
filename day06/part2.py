import sys

from common import move, setup, turn

at, pos, dir = setup([line.rstrip() for line in sys.stdin])


def findloop(
    pos: tuple[int, int],
    dir: tuple[int, int],
    obstacle: tuple[int, int],
    figures: set[tuple[tuple[int, int], tuple[int, int]]],
) -> bool:
    figures = set(figures)
    while True:
        new_pos = move(pos, dir)
        new_val = at(new_pos)
        if not new_val:
            break
        if new_val == "#" or new_pos == obstacle:
            dir = turn(dir)
        else:
            pos = new_pos
        if (pos, dir) in figures:
            return True
        figures.add((pos, dir))
    return False


places = {pos}
figures = {(pos, dir)}

total = 0

while True:
    new_pos = move(pos, dir)
    new_val = at(new_pos)
    if not new_val:
        break
    if new_val == "#":
        dir = turn(dir)
    else:
        if new_pos not in places:
            total += findloop(pos, dir, new_pos, figures)
            places.add(new_pos)
        pos = new_pos
    figures.add((pos, dir))

assert total == 1740
