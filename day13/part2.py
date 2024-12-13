from common import Point, machines, solve


def farprize(a: Point, b: Point, p: Point) -> tuple[Point, Point, Point]:
    return (a, b, (p[0] + 10000000000000, p[1] + 10000000000000))


total = sum(solve(*farprize(*machine)) for machine in machines())

assert total == 93209116744825
