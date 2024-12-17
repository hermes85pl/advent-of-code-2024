import sys
from itertools import takewhile

from common import DIRS, Point, setup

m = [[x for x in line.rstrip()] for line in takewhile(lambda l: l != "\n", sys.stdin)]

move_marks = [x for line in sys.stdin for x in line.rstrip()]

at, locate, locateall, move, put = setup(m)

pos = locate("@")


def find_space(pos: Point, dir: Point) -> Point | None:
    while True:
        pos = move(pos, dir)
        val = at(pos)
        if val == "#":
            break
        if val == "O":
            continue
        return pos
    return None


def move_boxes(pos: Point, dir: Point) -> bool:
    if new_pos := find_space(pos, dir):
        put(new_pos, "O")
        put(pos, ".")
        return True
    return False


for move_mark in move_marks:
    dir = DIRS[move_mark]
    new_pos = move(pos, dir)
    new_val = at(new_pos)
    if new_val == "#" or new_val == "O" and not move_boxes(new_pos, dir):
        continue
    pos = new_pos

total = sum(100 * i + j for i, j in locateall("O"))

assert total == 1552879
