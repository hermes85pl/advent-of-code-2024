from common import bootstrap

antenas, fits = bootstrap()


def antinodes():
    for k, v in antenas.items():
        for i, p0 in enumerate(v):
            for p1 in v[i + 1 :]:
                dh = p1[0] - p0[0]
                dw = p1[1] - p0[1]
                yield from (
                    pos
                    for pos in ((p0[0] - dh, p0[1] - dw), (p1[0] + dh, p1[1] + dw))
                    if fits(pos)
                )


total = len(set(antinodes()))

assert total == 256
