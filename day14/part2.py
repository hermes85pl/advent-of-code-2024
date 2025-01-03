from common import XMAX, XMID, YMAX, YMID, Point, place, robots


def distance_from_the_center(pos: Point) -> float:
    return abs(pos[0] - XMID) + abs(pos[1] - YMID)


robots_initially = list(robots())
min_distance = None
answer = None

for t in range(XMAX * YMAX):
    new_distance = sum(
        distance_from_the_center(place(pos, vel, t))
        for pos, vel in robots_initially[::5]
    )
    if min_distance is None or new_distance < min_distance:
        min_distance = new_distance
        answer = t

assert answer == 6876
