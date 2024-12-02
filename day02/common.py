def safe(levels: list[int]) -> bool:
    prev_sign = 0
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]

        if diff == 0:
            return False

        sign = diff // abs(diff)
        if prev_sign == 0:
            prev_sign = sign
        elif sign != prev_sign:
            return False

        if abs(diff) > 3:
            return False
    return True
