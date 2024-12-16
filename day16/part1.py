from heapq import heappop, heappush

from common import Point, setup

at, locate, move, turn = setup()

pos = locate("S")

dir: Point = (0, 1)

figure_to_score_map: dict[tuple[Point, Point], int] = {}
score_figure_queue: list[tuple[int, Point, Point]] = [(0, pos, dir)]

min_score = None

while score_figure_queue:
    score, pos, dir = heappop(score_figure_queue)
    val = at(pos)
    if val == "#":
        continue
    if val == "E":
        min_score = score
        break
    if (
        prev_score := figure_to_score_map.get((pos, dir))
    ) is not None and score >= prev_score:
        continue
    figure_to_score_map[(pos, dir)] = score
    heappush(score_figure_queue, (score + 1, move(pos, dir), dir))
    for clockwise in (True, False):
        heappush(score_figure_queue, (score + 1000, pos, turn(dir, clockwise)))

assert min_score == 98416
