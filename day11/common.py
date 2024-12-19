from functools import cache


def _blink1(stone: int):
    if stone == 0:
        yield 1
    else:
        s = str(stone)
        slen = len(s)
        if slen % 2 == 0:
            slen2 = slen // 2
            yield int(s[:slen2])
            yield int(s[slen2:])
        else:
            yield 2024 * stone


@cache
def blinknlen(stone: int, count: int) -> int:
    return (
        sum(1 for _ in _blink1(stone))
        if count == 1
        else sum(blinknlen(x, count - 1) for x in _blink1(stone))
    )
