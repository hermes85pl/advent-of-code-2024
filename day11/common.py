def blink1(stone: int):
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


memory: dict[tuple[int, int], int] = {}


def blinknlen(stone: int, count: int) -> int:
    key = (stone, count)
    try:
        return memory[key]
    except KeyError:
        result = (
            sum(1 for _ in blink1(stone))
            if count == 1
            else sum(blinknlen(x, count - 1) for x in blink1(stone))
        )
        memory[key] = result
        return result