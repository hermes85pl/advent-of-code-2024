from common import XMAX, XMID, YMAX, YMID, place, robots


def distance_from_the_center(pos: tuple[int, int]) -> float:
    return (abs(pos[0] - XMID) ** 2 + abs(pos[1] - YMID) ** 2) ** 0.5


robots_initially = list(robots())
min_distance = None
answer = None

for t in range(XMAX * YMAX):
    new_distance = sum(
        distance_from_the_center(place(pos, vel, t))
        for pos, vel in robots_initially[::3]
    )
    if min_distance is None or new_distance < min_distance:
        min_distance = new_distance
        answer = t

assert answer == 6876
