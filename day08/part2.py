from common import bootstrap

antenas, fits = bootstrap()


def move(pos: tuple[int, int], dir: tuple[int, int]):
    while fits(pos):
        yield pos
        pos = (pos[0] + dir[0], pos[1] + dir[1])


def antinodes():
    for k, v in antenas.items():
        for i, p0 in enumerate(v):
            for p1 in v[i + 1 :]:
                dh = p1[0] - p0[0]
                dw = p1[1] - p0[1]
                yield from move(p0, (-dh, -dw))
                yield from move(p1, (dh, dw))


total = len(set(antinodes()))

assert total == 1005
